from django.shortcuts import render, redirect
from .forms import DivorceSammelanFormForm
from .models import DivorceSammelanForm

def divorce_sammelan_form_view(request):
    if request.method == 'POST':
        form = DivorceSammelanFormForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form and get the instance
            registration = form.save()
            # Pass the saved registration data to success page
            return render(request, 'biodata/divorce_sammelan_success.html', {
                'registration': registration,
                'name': registration.name,
                'email': registration.email,
                'regMobile': registration.regMobile,
                'registration_id': registration.id,
            })
        else:
            # If form has errors, re-render with errors
            print("Form Errors:", form.errors)  # Debug: print errors to console
            return render(request, 'biodata/divorce_sammelan_form.html', {
                'form': form,
                'errors': form.errors
            })
    else:
        form = DivorceSammelanFormForm()
    return render(request, 'biodata/divorce_sammelan_form.html', {'form': form})


from .forms import FortyPlusSammelanForm
from .models import FortyPlusSammelan

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
