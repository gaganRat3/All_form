import re
from datetime import datetime, date
from django.shortcuts import render, redirect
from django.contrib import messages
from .models_samuh_janoi import SamuhJanoiRegistration


def parse_dob(dob_str):
    if not dob_str:
        return None
    dob_str = dob_str.strip()
    formats = ['%d-%m-%Y', '%d/%m/%Y', '%Y-%m-%d', '%Y/%m/%d']
    for fmt in formats:
        try:
            return datetime.strptime(dob_str, fmt).date()
        except ValueError:
            pass
    return None


def clean_phone_number(val):
    if not val:
        return ""
    clean = re.sub(r'[\s\-\(\)]', '', str(val).strip())
    if clean.startswith('+91'):
        clean = clean[3:]
    elif clean.startswith('91') and len(clean) == 12:
        clean = clean[2:]
    elif clean.startswith('0') and len(clean) == 11:
        clean = clean[1:]
    return clean


def samuh_janoi_form_view(request):
    if request.method == 'POST':
        data = request.POST
        batuk_name = data.get('batuk_name', '').strip()
        batuk_dob_raw = data.get('batuk_dob', '').strip()
        mother_name = data.get('mother_name', '').strip()
        father_name = data.get('father_name', '').strip()
        sub_caste = data.get('sub_caste', '').strip()
        gotra = data.get('gotra', '').strip()
        home_address = data.get('home_address', '').strip()
        village_city = data.get('village_city', '').strip()
        phone_raw = data.get('phone_number', '').strip()
        whatsapp_raw = data.get('whatsapp_number', '').strip()

        errors = {}

        # 1. Batuk Name
        if not batuk_name:
            errors['batuk_name'] = 'કૃપા કરીને બટુકનું પૂરું નામ દાખલ કરો. (Please enter Batuk\'s full name)'

        # 2. Batuk DOB
        parsed_dob = parse_dob(batuk_dob_raw)
        if not batuk_dob_raw:
            errors['batuk_dob'] = 'કૃપા કરીને બટુકની જન્મ-તારીખ પસંદ કરો. (Please select Batuk\'s date of birth)'
        elif not parsed_dob:
            errors['batuk_dob'] = 'અમાન્ય જન્મ તારીખ. કૃપા કરીને સાચી તારીખ દાખલ કરો. (Invalid date format)'
        elif parsed_dob > date.today():
            errors['batuk_dob'] = 'જન્મ તારીખ ભવિષ્યની ન હોઈ શકે. (Date of birth cannot be in the future)'

        # 3. Mother Name
        if not mother_name:
            errors['mother_name'] = 'કૃપા કરીને બટુકની માતાનું પૂરું નામ દાખલ કરો. (Please enter Mother\'s full name)'

        # 4. Father Name
        if not father_name:
            errors['father_name'] = 'કૃપા કરીને બટુકના પિતાનું પૂરું નામ દાખલ કરો. (Please enter Father\'s full name)'

        # 5. Sub-Caste
        if not sub_caste:
            errors['sub_caste'] = 'કૃપા કરીને બ્રાહ્મણ પેટા-જ્ઞાતિ જણાવો. (Please specify Brahmin sub-caste)'

        # 6. Gotra
        if not gotra:
            errors['gotra'] = 'કૃપા કરીને આપનું ગૌત્ર જણાવો. (Please enter Gotra)'

        # 7. Home Address
        if not home_address:
            errors['home_address'] = 'કૃપા કરીને પિનકોડ સાથે ઘરનું સરનામું લખો. (Please enter home address with pincode)'

        # 8. Village / City
        if not village_city:
            errors['village_city'] = 'કૃપા કરીને આપનું ગામ અથવા શહેરનું નામ લખો. (Please enter village or city)'

        # 9. Phone Number
        clean_phone = clean_phone_number(phone_raw)
        if not phone_raw:
            errors['phone_number'] = 'કૃપા કરીને ફોન નંબર દાખલ કરો. (Phone number is required)'
        elif not (clean_phone.isdigit() and len(clean_phone) == 10):
            errors['phone_number'] = 'કૃપા કરીને માન્ય ૧૦ આંકડાનો ફોન નંબર દાખલ કરો. (Enter valid 10-digit phone number)'

        # 10. WhatsApp Number
        clean_whatsapp = clean_phone_number(whatsapp_raw)
        if not whatsapp_raw:
            errors['whatsapp_number'] = 'કૃપા કરીને વોટ્સએપ નંબર દાખલ કરો. (WhatsApp number is required)'
        elif not (clean_whatsapp.isdigit() and len(clean_whatsapp) == 10):
            errors['whatsapp_number'] = 'કૃપા કરીને માન્ય ૧૦ આંકડાનો વોટ્સએપ નંબર દાખલ કરો. (Enter valid 10-digit WhatsApp number)'

        if errors:
            return render(request, 'biodata/Samuh_Janoi.html', {
                'errors': errors,
                'form_data': data,
            })

        # Save record
        registration = SamuhJanoiRegistration.objects.create(
            batuk_name=batuk_name,
            batuk_dob=parsed_dob,
            mother_name=mother_name,
            father_name=father_name,
            sub_caste=sub_caste,
            gotra=gotra,
            home_address=home_address,
            village_city=village_city,
            phone_number=clean_phone if (clean_phone.isdigit() and len(clean_phone) == 10) else phone_raw,
            whatsapp_number=clean_whatsapp if (clean_whatsapp.isdigit() and len(clean_whatsapp) == 10) else whatsapp_raw,
        )

        # Store in session for success display
        request.session['samuh_janoi_id'] = registration.id
        return redirect('samuh_janoi_success')

    return render(request, 'biodata/Samuh_Janoi.html')


def samuh_janoi_success_view(request):
    registration_id = request.session.get('samuh_janoi_id')
    registration = None
    if registration_id:
        try:
            registration = SamuhJanoiRegistration.objects.get(id=registration_id)
        except SamuhJanoiRegistration.DoesNotExist:
            registration = None

    return render(request, 'biodata/Samuh_Janoi_success.html', {
        'registration': registration,
    })
