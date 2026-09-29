import razorpay
from django.conf import settings
from django.shortcuts import render, redirect
from django.db import OperationalError
from django.http import HttpResponseBadRequest

from .forms import SamstaGujaratRegistrationForm

# Initialize Razorpay Client
razorpay_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)

def samsta_gujarat_form_view(request):
    """Separate backend logic for the Samsta Gujarat registration form."""
    if request.method == 'POST':
        form = SamstaGujaratRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Verify Razorpay signature
                razorpay_payment_id = request.POST.get('razorpay_payment_id', '')
                razorpay_order_id = request.POST.get('razorpay_order_id', '')
                razorpay_signature = request.POST.get('razorpay_signature', '')
                
                params_dict = {
                    'razorpay_order_id': razorpay_order_id,
                    'razorpay_payment_id': razorpay_payment_id,
                    'razorpay_signature': razorpay_signature
                }
                
                payment_status = 'pending'
                if razorpay_payment_id and razorpay_signature:
                    try:
                        razorpay_client.utility.verify_payment_signature(params_dict)
                        payment_status = 'paid'
                    except razorpay.errors.SignatureVerificationError:
                        return HttpResponseBadRequest("Invalid Payment Signature")

                registration = form.save(commit=False)
                registration.payment_status = payment_status
                registration.save()
                
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

    # GET Request: Create Razorpay Order
    amount = 700 * 100  # Rs 700 in paise
    currency = "INR"
    
    try:
        razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))
        razorpay_order_id = razorpay_order['id']
    except Exception as e:
        print(f"Razorpay Order Error: {e}")
        razorpay_order_id = ""

    form = SamstaGujaratRegistrationForm()
    return render(request, 'biodata/samsta_gujarat_form.html', {
        'form': form,
        'razorpay_order_id': razorpay_order_id,
        'razorpay_amount': amount,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
    })

def samsta_gujarat_success(request):
    """Success page after successful Samsta Gujarat registration."""
    return render(request, 'biodata/samsta_gujarat_success.html')
