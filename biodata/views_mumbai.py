
from django.shortcuts import render, redirect
from .models import MumbaiMaharashtraBiodata
from django.core.files.storage import default_storage

def mumbai_maharashtra_view(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        # Save uploaded photo
        photo = files.get('photo')
        instance = MumbaiMaharashtraBiodata(
            name=data.get('name'),
            gender=data.get('gender'),
            dob=data.get('dob'),
            marital=data.get('marital'),
            disability=data.get('disability'),
            tob=data.get('tob'),
            birthPlace=data.get('birthPlace'),
            city=data.get('city'),
            country=data.get('country'),
            visa=data.get('visa'),
            height=data.get('height'),
            weight=data.get('weight'),
            education=data.get('education'),
            educationDetail=data.get('educationDetail'),
            occupationCat=data.get('occupationCat'),
            occupationDetails=data.get('occupationDetails'),
            salary=data.get('salary'),
            shani=data.get('shani'),
            hobbies=data.get('hobbies'),
            father=data.get('father'),
            mother=data.get('mother'),
            fatherWp=data.get('fatherWp'),
            motherWp=data.get('motherWp'),
            caste=data.get('caste'),
            gotra=data.get('gotra'),
            kuldevi=data.get('kuldevi'),
            siblings=data.get('siblings'),
            eating_habbits=data.get('eating_habbits'),
            alcohol=data.get('alcohol'),
            smoke=data.get('smoke'),
            other_habbit=data.get('other_habbit'),
            legal_case=data.get('legal_case'),
            locChoice=data.get('locChoice'),
            ageGap=data.get('ageGap'),
            eduChoice=data.get('eduChoice'),
            otherChoice=data.get('otherChoice'),
            who=data.get('who'),
            regMobile=data.get('regMobile'),
            resCat=data.get('resCat'),
            nadi=data.get('nadi'),
            email=data.get('email'),
            whatsapp=data.get('whatsapp'),
            declaration=data.get('declaration'),
        )
        if photo:
            instance.photo = photo
        instance.save()
        return redirect('mumbai_maharashtra_success')
    return render(request, 'biodata/mumbai_Maharashtra.html')

def mumbai_maharashtra_success(request):
    return render(request, 'biodata/mumbai_maharashtra_success.html')
