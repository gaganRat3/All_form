from types import SimpleNamespace

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from .models_nri_sammelan import NriSammelanBiodata


def validate_mobile(mobile):
    return bool(mobile) and len(mobile) == 10 and mobile.isdigit()


def validate_registrant_mobile(mobile):
    return bool(mobile) and len(mobile) >= 10 and mobile.isdigit()


def validate_email(email):
    return bool(email) and '@' in email and '.' in email


def build_form_data(data):
    return {key: SimpleNamespace(value=value) for key, value in data.items()}


def build_prefill_data(data):
    return {
        key: value
        for key, value in data.items()
        if key != 'csrfmiddlewaretoken'
    }


def nri_sammelan_form_view(request):
    residence_choices = [
        ('mumbai_maharashtra', 'Mumbai & Maharashtra Region'),
        ('rest_of_india', 'Rest of Indian Region (except Gujarat & Maharashtra)'),
        ('nri', 'NRI (Any Visa)'),
    ]

    if request.method == 'POST':
        data = request.POST.copy()
        photo = request.FILES.get('photo')
        errors = {}

        if not data.get('name') or len(data.get('name', '')) < 3:
            errors['name'] = 'Please enter a valid full name (minimum 3 characters)'
        if not data.get('gender'):
            errors['gender'] = 'Please select a gender'
        if not data.get('dob'):
            errors['dob'] = 'Please enter date of birth'
        if not data.get('email') or not validate_email(data.get('email', '')):
            errors['email'] = 'Please enter a valid email address'
        if not data.get('regMobile') or not validate_registrant_mobile(data.get('regMobile', '')):
            errors['regMobile'] = 'Please enter a valid mobile number with at least 10 digits'
        if not data.get('whatsapp') or not validate_mobile(data.get('whatsapp', '')):
            errors['whatsapp'] = 'Please enter a valid 10-digit WhatsApp number'

        if not data.get('education'):
            errors['education'] = 'Please select your education'
        elif data.get('education') not in dict(NriSammelanBiodata.EDUCATION_CHOICES):
            errors['education'] = 'Invalid education option selected'

        res_cat = data.get('resCat')
        if not res_cat:
            errors['resCat'] = 'Please select your residence area'
        elif res_cat not in dict(residence_choices):
            errors['resCat'] = 'Invalid residence area selected'

        if not photo:
            errors['photo'] = 'Please upload a photo'
        else:
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
            if not any(photo.name.lower().endswith(ext) for ext in valid_extensions):
                errors['photo'] = 'Please upload a valid image file (JPG, PNG, GIF)'
            elif photo.size > 5 * 1024 * 1024:
                errors['photo'] = 'Photo size must be less than 5MB'

        if not data.get('declaration') or data.get('declaration') != 'Agree':
            errors['declaration'] = 'You must agree to the declaration to register'

        if errors:
            context = {
                'form': build_form_data(data),
                'errors': errors,
                'residence_choices': residence_choices,
                'selected_rescat': data.get('resCat', ''),
                'prefill_data': build_prefill_data(data),
                'first_error_field': next(iter(errors), ''),
                'error_fields': list(errors.keys()),
            }
            return render(request, 'biodata/nri_sammelan_form.html', context)

        try:
            instance = NriSammelanBiodata()
            for field in NriSammelanBiodata._meta.fields:
                field_name = field.name
                if field_name == 'photo' and photo:
                    instance.photo = photo
                elif field_name in data:
                    setattr(instance, field_name, data.get(field_name))

            instance.full_clean()
            instance.save()
            messages.success(request, 'Your registration has been submitted successfully!')
            return redirect('nri_sammelan_success')
        except ValidationError as exc:
            model_errors = {}
            for field_name, message_list in exc.message_dict.items():
                if isinstance(message_list, list) and message_list:
                    model_errors[field_name] = message_list[0]
                else:
                    model_errors[field_name] = str(message_list)

            context = {
                'form': build_form_data(data),
                'errors': model_errors,
                'residence_choices': residence_choices,
                'selected_rescat': data.get('resCat', ''),
                'prefill_data': build_prefill_data(data),
                'first_error_field': next(iter(model_errors), ''),
                'error_fields': list(model_errors.keys()),
            }
            return render(request, 'biodata/nri_sammelan_form.html', context)
        except Exception as exc:
            context = {
                'form': build_form_data(data),
                'errors': {'general': f'Error saving registration: {str(exc)}'},
                'residence_choices': residence_choices,
                'selected_rescat': data.get('resCat', ''),
                'prefill_data': build_prefill_data(data),
                'first_error_field': 'general',
                'error_fields': ['general'],
            }
            return render(request, 'biodata/nri_sammelan_form.html', context)

    context = {
        'residence_choices': residence_choices,
        'selected_rescat': '',
        'prefill_data': {},
        'first_error_field': '',
        'error_fields': [],
    }
    return render(request, 'biodata/nri_sammelan_form.html', context)


def nri_sammelan_success(request):
    return render(request, 'biodata/nri_sammelan_success.html')