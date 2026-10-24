from django.shortcuts import render, redirect
from django.contrib import messages
from .models_diwali_gift import DiwaliGiftRegistration


def diwali_gift_form_view(request):
    if request.method == 'POST':
        data = request.POST
        candidate_name = data.get('candidateName', '').strip()
        dob = data.get('dob', '').strip()
        current_city = data.get('currentCity', '').strip()
        candidate_mobile = data.get('candidateMobile', '').strip()
        parents_mobile = data.get('parentsMobile', '').strip()
        contact_person = data.get('contactPerson', '').strip()
        address = data.get('address', '').strip()
        contact_mobile = data.get('contactMobile', '').strip()
        pincode = data.get('pincode', '').strip()

        errors = {}
        if not candidate_name:
            errors['candidateName'] = 'Candidate name is required.'
        if not dob:
            errors['dob'] = 'Date of birth is required.'
        if not current_city:
            errors['currentCity'] = 'Current city is required.'
        if not candidate_mobile or len(candidate_mobile) != 10 or not candidate_mobile.isdigit():
            errors['candidateMobile'] = 'Please enter a valid 10-digit mobile number.'
        if not parents_mobile or len(parents_mobile) != 10 or not parents_mobile.isdigit():
            errors['parentsMobile'] = 'Please enter a valid 10-digit mobile number.'
        if not contact_person:
            errors['contactPerson'] = 'Contact person name is required.'
        if not address:
            errors['address'] = 'Full address is required for courier delivery.'
        if not contact_mobile or len(contact_mobile) != 10 or not contact_mobile.isdigit():
            errors['contactMobile'] = 'Please enter a valid 10-digit mobile number.'
        if not pincode or len(pincode) != 6 or not pincode.isdigit():
            errors['pincode'] = 'Please enter a valid 6-digit area pincode.'

        if errors:
            return render(request, 'biodata/Diwali_Gift_form.html', {
                'errors': errors,
                'form_data': data,
            })

        registration = DiwaliGiftRegistration.objects.create(
            candidate_name=candidate_name,
            dob=dob,
            current_city=current_city,
            candidate_mobile=candidate_mobile,
            parents_mobile=parents_mobile,
            contact_person=contact_person,
            address=address,
            contact_mobile=contact_mobile,
            pincode=pincode,
        )
        request.session['diwali_gift_candidate'] = registration.candidate_name
        request.session['diwali_gift_city'] = registration.current_city
        return redirect('diwali_gift_success')

    return render(request, 'biodata/Diwali_Gift_form.html')


def diwali_gift_success_view(request):
    candidate_name = request.session.get('diwali_gift_candidate', '')
    city = request.session.get('diwali_gift_city', '')
    return render(request, 'biodata/Diwali_Gift_success.html', {
        'candidate_name': candidate_name,
        'city': city,
    })

