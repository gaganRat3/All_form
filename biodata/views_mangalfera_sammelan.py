from django.shortcuts import render, redirect
from .forms_mangalfera_sammelan import MangalferaSammelanBiodataForm


def mangalfera_sammelan_form_view(request):
    """Display closed Mangalfera Sammelan registration form"""
    return render(request, 'biodata/mangalfera_summelen_from.html', {'is_closed': True})


def mangalfera_sammelan_success(request):
    """Display Mangalfera Sammelan success confirmation page"""
    return render(request, 'biodata/mangalfera_summelen_success.html')

