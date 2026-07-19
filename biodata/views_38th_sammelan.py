from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from types import SimpleNamespace

from .models_38th_sammelan import Sammelan38Biodata


def validate_mobile(mobile):
    return bool(mobile) and len(mobile) == 10 and mobile.isdigit()


def validate_email(email):
    return bool(email) and '@' in email and '.' in email


def build_form_data(data):
    return {key: SimpleNamespace(value=value) for key, value in data.items()}


def sammelan_38th_form_view(request):
    residence_choices = [
        choice for choice in Sammelan38Biodata.RESIDENCE_CHOICES
        if choice[0] not in {'mumbai_maharashtra', 'rest_of_india', 'nri'}
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
        if not data.get('regMobile') or not validate_mobile(data.get('regMobile', '')):
            errors['regMobile'] = 'Please enter a valid 10-digit mobile number'
        if not data.get('whatsapp') or not validate_mobile(data.get('whatsapp', '')):
            errors['whatsapp'] = 'Please enter a valid 10-digit WhatsApp number'

        if not data.get('education'):
            errors['education'] = 'Please select your education'
        elif data.get('education') not in dict(Sammelan38Biodata.EDUCATION_CHOICES):
            errors['education'] = 'Invalid education option selected'

        res_cat = data.get('resCat')
        if not res_cat:
            errors['resCat'] = 'Please select your residence area'
        elif res_cat == 'rest_india':
            data['resCat'] = 'rest_of_india'
        elif res_cat not in dict(Sammelan38Biodata.RESIDENCE_CHOICES):
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
            }
            return render(request, 'biodata/38th_sammelan_form.html', context)

        try:
            instance = Sammelan38Biodata()
            for field in Sammelan38Biodata._meta.fields:
                field_name = field.name
                if field_name == 'photo' and photo:
                    instance.photo = photo
                elif field_name in data:
                    setattr(instance, field_name, data.get(field_name))

            instance.full_clean()
            instance.save()
            messages.success(request, 'Your registration has been submitted successfully!')
            return redirect('38th_sammelan_success')
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
            }
            return render(request, 'biodata/38th_sammelan_form.html', context)
        except Exception as exc:
            context = {
                'form': build_form_data(data),
                'errors': {'general': f'Error saving registration: {str(exc)}'},
                'residence_choices': residence_choices,
                'selected_rescat': data.get('resCat', ''),
            }
            return render(request, 'biodata/38th_sammelan_form.html', context)

    context = {
        'residence_choices': residence_choices,
        'selected_rescat': '',
    }
    return render(request, 'biodata/38th_sammelan_form.html', context)


def sammelan_38th_success(request):
    return render(request, 'biodata/38th_sammelan_success.html')
