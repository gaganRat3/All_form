from django.shortcuts import render
from django.db import OperationalError
from .forms import FortyPlusSammelanForm, SaurasthraKutchSammelanForm
from .models import FortyPlusSammelan, SaurasthraKutchSammelan

def forty_plus_sammelan_form_view(request):
    """View for 40+ Sammelan registration form (separate backend)"""
    if request.method == 'POST':
        form = FortyPlusSammelanForm(request.POST, request.FILES)
        if form.is_valid():
            registration = form.save()
            return render(request, 'biodata/40plus_sammelan_success.html', {
                'registration': registration,
                'name': registration.name,
                'email': registration.email,
                'regMobile': registration.regMobile,
                'registration_id': registration.id,
            })
        else:
            print("Form Errors:", form.errors)
            return render(request, 'biodata/40+_sammelan_Form.html', {
                'form': form,
                'errors': form.errors
            })
    else:
        form = FortyPlusSammelanForm()
    return render(request, 'biodata/40+_sammelan_Form.html', {'form': form})


def saurashtra_kutch_sammelan_form_view(request):
    """View for Saurashtra & Kutch Sammelan registration form (separate backend)"""
    if request.method == 'POST':
        form = SaurasthraKutchSammelanForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                registration = form.save()
                return render(request, 'biodata/saurashtra_kutch_success.html', {
                    'registration': registration,
                    'name': registration.name,
                    'email': registration.email,
                    'regMobile': registration.regMobile,
                    'registration_id': registration.id,
                })
            except OperationalError as e:
                print(f"DATABASE ERROR: {e}")
                return render(request, 'biodata/saurashtra_kutch_form.html', {
                    'form': form,
                    'errors': {'Database Error': [f'Table missing. Run: python manage.py migrate. Details: {e}']}
                })
        else:
            print("Form Errors:", form.errors)
            return render(request, 'biodata/saurashtra_kutch_form.html', {
                'form': form,
                'errors': form.errors
            })
    else:
        form = SaurasthraKutchSammelanForm()
    return render(request, 'biodata/saurashtra_kutch_form.html', {'form': form})
