from django.shortcuts import render, redirect
from .forms_mangalfera_sammelan import MangalferaSammelanBiodataForm


def mangalfera_sammelan_form_view(request):
    """Display and process Mangalfera Sammelan registration form"""
    errors = None
    if request.method == 'POST':
        form = MangalferaSammelanBiodataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mangalfera_sammelan_success')
        else:
            errors = form.errors
    else:
        form = MangalferaSammelanBiodataForm()
    return render(request, 'biodata/mangalfera_summelen_from.html', {'form': form, 'errors': errors})


def mangalfera_sammelan_success(request):
    """Display Mangalfera Sammelan success confirmation page"""
    return render(request, 'biodata/mangalfera_summelen_success.html')

