from datetime import date, datetime

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from .models_marriage_done import MarriageDoneGiftSubmission


def _parse_date(value):
    if not value:
        return None
    value = value.strip()
    for date_format in ('%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y'):
        try:
            return datetime.strptime(value, date_format).date()
        except ValueError:
            continue

    # Accept non-zero-padded formats like 9-8-2003 or 9/8/2003.
    normalized = value.replace('/', '-')
    parts = normalized.split('-')
    if len(parts) == 3 and all(part.isdigit() for part in parts):
        try:
            if len(parts[0]) == 4:
                year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
            else:
                day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
            return date(year, month, day)
        except ValueError:
            return None

    return None


def marriage_done_form_view(request):
    if request.method == 'POST':
        data = request.POST.copy()
        photo = request.FILES.get('wedding_photo')
        errors = {}

        required_fields = [
            'filler_name',
            'relation',
            'mobile',
            'candidate_name',
            'gender',
            'candidate_dob',
            'spouse_name',
            'spouse_dob',
        ]
        for field_name in required_fields:
            if not data.get(field_name):
                errors[field_name] = 'This field is required.'

        if data.get('mobile') and (not data.get('mobile').isdigit() or len(data.get('mobile', '')) != 10):
            errors['mobile'] = 'Please enter a valid 10-digit mobile number.'

        if data.get('gender') and data.get('gender') not in dict(MarriageDoneGiftSubmission.GENDER_CHOICES):
            errors['gender'] = 'Please select a valid gender.'

        candidate_dob = _parse_date(data.get('candidate_dob', ''))
        spouse_dob = _parse_date(data.get('spouse_dob', ''))
        if data.get('candidate_dob') and not candidate_dob:
            errors['candidate_dob'] = 'Please enter a valid candidate date of birth.'
        if data.get('spouse_dob') and not spouse_dob:
            errors['spouse_dob'] = 'Please enter a valid spouse date of birth.'

        if not photo:
            errors['wedding_photo'] = 'Please upload a wedding photo.'
        else:
            valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
            if not photo.name.lower().endswith(valid_extensions):
                errors['wedding_photo'] = 'Please upload a valid image file.'
            elif photo.size > 5 * 1024 * 1024:
                errors['wedding_photo'] = 'Photo size must be less than 5MB.'

        if errors:
            return render(request, 'biodata/Marriage_done.html', {'form': data, 'errors': errors})

        try:
            submission = MarriageDoneGiftSubmission(
                filler_name=data.get('filler_name', '').strip(),
                relation=data.get('relation', '').strip(),
                mobile=data.get('mobile', '').strip(),
                candidate_name=data.get('candidate_name', '').strip(),
                gender=data.get('gender', ''),
                candidate_dob=candidate_dob,
                spouse_name=data.get('spouse_name', '').strip(),
                spouse_dob=spouse_dob,
                wedding_photo=photo,
            )
            submission.full_clean()
            submission.save()
            messages.success(request, 'Your marriage done form has been submitted successfully.')
            return redirect('marriage_done_success')
        except ValidationError as exc:
            model_errors = {}
            for field_name, message_list in exc.message_dict.items():
                model_errors[field_name] = message_list[0] if isinstance(message_list, list) and message_list else str(message_list)
            return render(request, 'biodata/Marriage_done.html', {'form': data, 'errors': model_errors})
        except Exception as exc:
            return render(request, 'biodata/Marriage_done.html', {'form': data, 'errors': {'general': str(exc)}})

    return render(request, 'biodata/Marriage_done.html', {'form': {}, 'errors': {}})


def marriage_done_success(request):
    return render(request, 'biodata/marriage_done_success.html')
