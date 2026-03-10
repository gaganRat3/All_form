import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Submission


def form_page(request):
    """Renders the blank test form."""
    return render(request, 'test_form/form.html')


def success_page(request):
    """Renders the success confirmation page."""
    return render(request, 'test_form/success.html')


@require_http_methods(["POST"])
def submit_form(request):
    """
    Receives POST data (multipart/form-data) from the JS fetch request.
    Validates fields, saves the Submission to the database,
    stores the uploaded image in /media/profile_images/,
    and returns a JSON response that the JS uses to redirect.
    """
    name    = request.POST.get('name', '').strip()
    email   = request.POST.get('email', '').strip()
    city    = request.POST.get('city', '').strip()
    message = request.POST.get('message', '').strip()
    image   = request.FILES.get('profile_image')

    # --- Simple server-side validation ---
    errors = {}
    if not name:
        errors['name'] = 'Name is required.'
    if not email:
        errors['email'] = 'Email is required.'
    if not city:
        errors['city'] = 'City is required.'
    if not message:
        errors['message'] = 'Message is required.'
    if not image:
        errors['profile_image'] = 'Profile image is required.'

    if errors:
        return JsonResponse({'status': 'error', 'errors': errors}, status=400)

    # --- Save to database ---
    submission = Submission.objects.create(
        name=name,
        email=email,
        city=city,
        message=message,
        profile_image=image,
    )

    return JsonResponse({
        'status': 'ok',
        'submission_id': submission.id,
        'redirect': '/test/success/',
    })
