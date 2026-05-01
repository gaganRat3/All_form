from django.shortcuts import render, redirect
from .forms_referral_program import ReferralProgramForm

def join_referral_program(request):
    if request.method == 'POST':
        form = ReferralProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'biodata/referral_success.html')
    else:
        form = ReferralProgramForm()
    return render(request, 'biodata/referral_form.html', {'form': form})
