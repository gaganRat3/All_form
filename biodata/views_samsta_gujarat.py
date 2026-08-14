from django.shortcuts import render, redirect
from django.db import OperationalError

from .forms import SamstaGujaratRegistrationForm


def samsta_gujarat_form_view(request):
    """Separate backend logic for the Samsta Gujarat registration form."""
    if request.method == 'POST':
        form = SamstaGujaratRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                registration = form.save()
                return render(request, 'biodata/samsta_gujarat_success.html', {
                    'registration': registration,
                    'name': registration.name,
                    'email': registration.email,
                    'regMobile': registration.regMobile,
                    'registration_id': registration.id,
                })
            except OperationalError as exc:
                print(f"DATABASE ERROR: {exc}")
                return render(request, 'biodata/samsta_gujarat_form.html', {
                    'form': form,
                    'errors': {'Database Error': [f'Table missing. Run: python manage.py migrate. Details: {exc}']}
                })
        else:
            return render(request, 'biodata/samsta_gujarat_form.html', {
                'form': form,
                'errors': form.errors,
            })

    form = SamstaGujaratRegistrationForm()
    return render(request, 'biodata/samsta_gujarat_form.html', {'form': form})


def samsta_gujarat_success(request):
    """Success page after successful Samsta Gujarat registration."""
    return render(request, 'biodata/samsta_gujarat_success.html')
