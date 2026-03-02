from django.shortcuts import render
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
