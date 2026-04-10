from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models_37th_sammelan import Sammelan37MumbaiMaharashtra
from django.core.files.storage import FileSystemStorage
import os

def validate_mobile(mobile):
    """Validate mobile number (10 digits)"""
    if not mobile or len(mobile) != 10 or not mobile.isdigit():
        return False
    return True

def validate_email(email):
    """Basic email validation"""
    if '@' not in email or '.' not in email:
        return False
    return True

def sammelan_37_mumbai_maharashtra_view(request):
    if request.method == 'POST':
        data = request.POST.copy()
        photo = request.FILES.get('photo')
        errors = {}
        
        # Validation
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
        
        if not data.get('resCat'):
            errors['resCat'] = 'Please select your residence area'
        elif data.get('resCat') not in dict(Sammelan37MumbaiMaharashtra.RESIDENCE_CHOICES):
            errors['resCat'] = 'Invalid residence area selected'
        
        if not photo:
            errors['photo'] = 'Please upload a photo'
        else:
            # Validate photo
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
            if not any(photo.name.lower().endswith(ext) for ext in valid_extensions):
                errors['photo'] = 'Please upload a valid image file (JPG, PNG, GIF)'
            elif photo.size > 5 * 1024 * 1024:  # 5MB
                errors['photo'] = 'Photo size must be less than 5MB'
        
        if not data.get('declaration') or data.get('declaration') != 'Agree':
            errors['declaration'] = 'You must agree to the declaration to register'
        
        # If there are errors, return form with error messages
        if errors:
            context = {
                'form': data,
                'errors': errors
            }
            return render(request, 'biodata/37_sammelan_UK_europe.html', context)
        
        # If validation passes, save the data
        try:
            instance = Sammelan37MumbaiMaharashtra()
            for field in Sammelan37MumbaiMaharashtra._meta.fields:
                fname = field.name
                if fname == 'photo' and photo:
                    instance.photo = photo
                elif fname in data:
                    setattr(instance, fname, data.get(fname))
            instance.save()
            messages.success(request, 'Your registration has been submitted successfully!')
            return redirect('37th_sammelan_mumbai_maharashtra_success')
        except Exception as e:
            context = {
                'form': data,
                'errors': {'general': f'Error saving registration: {str(e)}'}
            }
            return render(request, 'biodata/37_sammelan_UK_europe.html', context)
    
    return render(request, 'biodata/37_sammelan_UK_europe.html')

def sammelan_37_mumbai_maharashtra_success(request):
    return render(request, 'biodata/37_sammelan_success.html')
