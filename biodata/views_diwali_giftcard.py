from django.shortcuts import render, redirect
from .models_diwali_giftcard import DiwaliGiftCard


def diwali_giftcard_form_view(request):
    if request.method == 'POST':
        data = request.POST
        candidate_name = data.get('candidateName', '').strip()
        website_name = data.get('websiteName', '').strip()
        membership_id = data.get('membershipId', '').strip()
        whatsapp_number = data.get('whatsappNumber', '').strip()
        home_address = data.get('homeAddress', '').strip()
        mobile_number = data.get('mobileNumber', '').strip()

        errors = {}
        if not candidate_name:
            errors['candidateName'] = 'Candidate Name is required.'
        if not website_name:
            errors['websiteName'] = 'Website Name is required.'
        if not membership_id:
            errors['membershipId'] = 'Membership ID is required.'
        if not whatsapp_number:
            errors['whatsappNumber'] = 'WhatsApp Number is required.'
        elif len(whatsapp_number) != 10 or not whatsapp_number.isdigit():
            errors['whatsappNumber'] = 'Please enter a valid 10-digit WhatsApp number.'
        if not mobile_number:
            errors['mobileNumber'] = 'Mobile Number is required.'
        elif len(mobile_number) != 10 or not mobile_number.isdigit():
            errors['mobileNumber'] = 'Please enter a valid 10-digit Mobile number.'
        if not home_address:
            errors['homeAddress'] = 'Home Address is required.'

        if errors:
            return render(request, 'biodata/Diwali_giftcard.html', {
                'errors': errors,
                'form_data': data,
            })

        gift_card = DiwaliGiftCard.objects.create(
            candidate_name=candidate_name,
            website_name=website_name,
            membership_id=membership_id,
            whatsapp_number=whatsapp_number,
            home_address=home_address,
            mobile_number=mobile_number,
        )

        request.session['diwali_giftcard_candidate'] = gift_card.candidate_name
        request.session['diwali_giftcard_membership'] = gift_card.membership_id
        request.session['diwali_giftcard_website'] = gift_card.website_name
        request.session['diwali_giftcard_mobile'] = gift_card.mobile_number
        return redirect('diwali_giftcard_success')

    return render(request, 'biodata/Diwali_giftcard.html')


def diwali_giftcard_success_view(request):
    candidate_name = request.session.get('diwali_giftcard_candidate', '')
    membership_id = request.session.get('diwali_giftcard_membership', '')
    website_name = request.session.get('diwali_giftcard_website', '')
    mobile_number = request.session.get('diwali_giftcard_mobile', '')
    return render(request, 'biodata/Diwali_giftcard_success.html', {
        'candidate_name': candidate_name,
        'membership_id': membership_id,
        'website_name': website_name,
        'mobile_number': mobile_number,
    })

