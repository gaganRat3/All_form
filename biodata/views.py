from .forms_picnic import PicnicRegistrationForm
from .models_picnic import PicnicRegistration
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from threading import Thread
import os

def send_picnic_registration_email_async(picnic_registration):
    """Send confirmation email asynchronously in background thread"""
    thread = Thread(
        target=send_picnic_registration_email,
        args=(picnic_registration,),
        daemon=True
    )
    thread.start()

def send_picnic_registration_email(picnic_registration):
    """Send confirmation email to user with all registration details"""
    try:
        subject = '✅ Picnic Registration Confirmation - Bhudev Network'
        
        # Create email context with all form data
        context = {
            'filler_name': picnic_registration.filler_name,
            'contact_number': picnic_registration.contact_number,
            'email_address': picnic_registration.email_address,
            'city': picnic_registration.city,
            'candidate_name': picnic_registration.candidate_name,
            'gender': picnic_registration.gender,
            'relation': picnic_registration.relation,
            'dob': picnic_registration.dob.strftime('%d-%m-%Y') if picnic_registration.dob else 'N/A',
            'persons': picnic_registration.persons,
            'is_coming': picnic_registration.is_coming,
            'submission_date': picnic_registration.submitted_at.strftime('%d-%m-%Y %H:%M:%S') if picnic_registration.submitted_at else 'N/A',
        }
        
        # Create HTML email content
        html_message = f"""
        <html>
            <head>
                <style>
                    body {{ font-family: 'Poppins', Arial, sans-serif; line-height: 1.6; color: #333; }}
                    .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                    .header {{ background: linear-gradient(135deg, #1E88E5, #00BCD4); color: white; padding: 20px; border-radius: 10px 10px 0 0; text-align: center; }}
                    .header h1 {{ margin: 0; font-size: 24px; }}
                    .content {{ background: #f8f9fa; padding: 20px; border-radius: 0 0 10px 10px; }}
                    .detail-row {{ display: grid; grid-template-columns: 150px 1fr; padding: 10px 0; border-bottom: 1px solid #ddd; }}
                    .detail-row:last-child {{ border-bottom: none; }}
                    .label {{ font-weight: 700; color: #1E88E5; }}
                    .value {{ color: #555; }}
                    .success-badge {{ display: inline-block; background: #4CAF50; color: white; padding: 8px 16px; border-radius: 20px; margin-bottom: 15px; }}
                    .footer {{ text-align: center; margin-top: 20px; font-size: 12px; color: #999; }}
                    .event-info {{ background: white; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid #1E88E5; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>🎉 Picnic Registration Confirmed!</h1>
                        <p>Bhudev Network - 1-Day Picnic ઉજાણી</p>
                    </div>
                    
                    <div class="content">
                        <div class="success-badge">✓ Successfully Registered</div>
                        
                        <div class="event-info">
                            <strong>📅 Event Details:</strong><br>
                            <strong>Date:</strong> 15-02-2026 (Sunday)<br>
                            <strong>Time:</strong> 9am to 5pm<br>
                            <strong>Place:</strong> Resort near Vadodara
                        </div>
                        
                        <h3 style="color: #1E88E5; border-bottom: 2px solid #1E88E5; padding-bottom: 10px;">Your Registration Details</h3>
                        
                        <div class="detail-row">
                            <div class="label">1. Name (Filler):</div>
                            <div class="value">{context['filler_name']}</div>
                        </div>
                        
                        <div class="detail-row">
                            <div class="label">2. Contact Number:</div>
                            <div class="value">{context['contact_number']}</div>
                        </div>
                        
                        <div class="detail-row">
                            <div class="label">3. Email Address:</div>
                            <div class="value">{context['email_address']}</div>
                        </div>
                        
                        <div class="detail-row">
                            <div class="label">4. City:</div>
                            <div class="value">{context['city']}</div>
                        </div>
                        
                        <div class="detail-row">
                            <div class="label">5. Candidate Name:</div>
                            <div class="value">{context['candidate_name']}</div>
                        </div>
                        
                        <div class="detail-row">
                            <div class="label">6. Gender:</div>
                            <div class="value">{context['gender']}</div>
                        </div>
                        
                        <div class="detail-row">
                            <div class="label">7. Relation:</div>
                            <div class="value">{context['relation']}</div>
                        </div>
                        
                        <div class="detail-row">
                            <div class="label">8. Date of Birth:</div>
                            <div class="value">{context['dob']}</div>
                        </div>
                        
                        <div class="detail-row">
                            <div class="label">9. No. of Persons:</div>
                            <div class="value">{context['persons']}</div>
                        </div>
                        
                        <div class="detail-row">
                            <div class="label">10. Is Coming:</div>
                            <div class="value">{context['is_coming']}</div>
                        </div>
                        
                        <div class="detail-row">
                            <div class="label">Submitted At:</div>
                            <div class="value">{context['submission_date']}</div>
                        </div>
                        
                        <div class="event-info" style="margin-top: 20px; background: #E8F5E9;">
                            <strong style="color: #2E7D32;">✓ Keep this email for reference</strong><br>
                            For further queries, contact us at: 9662766565, 9099798986, 6352144677
                        </div>
                    </div>
                    
                    <div class="footer">
                        <p>This is an automated email. Please do not reply to this email.</p>
                        <p>&copy; 2026 Bhudev Network. All rights reserved.</p>
                    </div>
                </div>
            </body>
        </html>
        """
        
        plain_message = strip_tags(html_message)
        
        # Create EmailMessage and attach the poster image
        email = EmailMessage(
            subject,
            html_message,
            settings.EMAIL_HOST_USER,
            [picnic_registration.email_address],
        )
        email.content_subtype = 'html'
        
        # Attach the poster image
        poster_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'poster_picnic.jpeg')
        if os.path.exists(poster_path):
            with open(poster_path, 'rb') as attachment:
                email.attach('poster_picnic.jpeg', attachment.read(), 'image/jpeg')
            print(f"Poster image attached to email")
        else:
            print(f"Warning: Poster image not found at {poster_path}")
        
        # Send email
        email.send(fail_silently=False)
        
        print(f"Confirmation email sent successfully to {picnic_registration.email_address}")
        return True
        
    except Exception as e:
        print(f"Error sending confirmation email: {str(e)}")
        return False

# Picnic Registration Form View
def picnic_registration_view(request):
    if request.method == 'POST':
        form = PicnicRegistrationForm(request.POST)
        if form.is_valid():
            try:
                picnic_registration = form.save()
                request.session['picnic_data'] = {
                    'filler_name': picnic_registration.filler_name,
                    'contact_number': picnic_registration.contact_number,
                    'email_address': picnic_registration.email_address,
                    'city': picnic_registration.city,
                    'candidate_name': picnic_registration.candidate_name,
                    'dob': str(picnic_registration.dob),
                    'persons': picnic_registration.persons,
                }
                request.session.modified = True
                
                # Send confirmation email asynchronously (non-blocking)
                send_picnic_registration_email_async(picnic_registration)
                
                return JsonResponse({'success': True, 'redirect_url': '/picnic-registration-confirmation/'})
            except Exception as e:
                print(f"Error saving form: {str(e)}")
                return JsonResponse({'success': False, 'errors': {'general': str(e)}}, status=400)
        else:
            # Convert form errors to a readable format
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = ', '.join([str(e) for e in error_list])
            print(f"Form validation errors: {errors}")
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = PicnicRegistrationForm()
    return render(request, 'biodata/picnic_registration_form.html', {'form': form})

def picnic_registration_confirmation(request):
    picnic_data = request.session.get('picnic_data', {})
    if not picnic_data:
        return redirect('picnic_registration_form')
    return render(request, 'biodata/picnic_registration_confirmation.html', {'picnic_data': picnic_data})
# Add missing imports
import json
import logging
from .bncf_form import BncBnfApplicationForm
from .models import BncBnfApplication, GarbaPassRegistration, AudienceRegistration
from .forms_garba_pass import GarbaPassRegistrationForm
from .forms_audience import AudienceRegistrationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import BhudevSammelanRegistration
from django import forms
from django.urls import reverse

# Divorce Sammelan Registration Form
class BhudevSammelanRegistrationForm(forms.ModelForm):
    class Meta:
        model = BhudevSammelanRegistration
        fields = '__all__'

def bhudev_sammelan_registration_view(request):
    declaration_map = {
        'Agree': 'agree',
        'Disagree': 'disagree',
    }
    if request.method == 'POST':
        # Map custom frontend fields to model fields
        # Map frontend values to model choices
        gender_map = {
            'Male': 'male',
            'Female': 'female',
            'Other': 'other',
        }
        marital_map = {
            'Never Married': 'never_married',
            'One Time Gol-Dhana But then Cancel': 'gol_dhana_cancel',
            'One Time Engagement (Vivah) but afterwards cancel': 'engagement_cancel',
            'Divorce': 'divorce',
            'Widow': 'widow',
        }
        print('DEBUG resCat:', request.POST.get('resCat'))
        print('DEBUG declaration:', request.POST.get('declaration'))
        rescat_map = {
            'Gujarat Region (North, Central, South)': 'gujarat',
            'Saurshtra - Kachchh Region': 'saurashtra',
            'Mumbai - Maharashtra - Rest of India Region': 'mumbai',
            'NRI (Non Residential Indian - Any Visa) Region (Out of India)': 'nri',
        }
        visa_map = {
            'Indian Citizen': 'indian_citizen',
            'NRI - Student Visa': 'nri_student_visa',
            'NRI - Work Permit': 'nri_work_permit',
            'NRI - PR': 'nri_pr',
            'NRI - PR In Process': 'nri_pr_in_process',
            'NRI - Green Card (USA)': 'nri_green_card_usa',
            'NRI - Blue Card (EU)': 'nri_blue_card_eu',
            'NRI - Citizenship': 'nri_citizenship',
            'NRI - Visitor Visa': 'nri_visitor_visa',
            'NRI - H1B (USA)': 'nri_h1b_usa',
            'NRI - Business Visa': 'nri_business_visa',
            'NRI - OCI': 'nri_oci',
            'NRI - F1': 'nri_f1',
        }
        education_map = {
            'Undergraduate (10th 12th Pass / Fail , Diploma , ITI , Not Completed Graduation)': 'undergraduate',
            'Graduate (BA , B.Com. , B.Sc. , BE , BTech, LLB , B. Arch., BBA , BCA etc)': 'graduate',
            'Masters (MA , MCom, MSc., ME , MTech, M.Arch , M.Phil, LLM, etc)': 'masters',
            'CA , CS , ICWA, CPA, ACCA , CIMA , etc': 'ca_cs',
            'Doctor - Medical - Pharmacy - Dentist - Physiotherapist - Paramedical - Nursing - Clinical Surgical - Specialists': 'doctor_medical',
            'PhD , UPSC, GPSC (IAS , IPS, etc) , Mayor , Civil Services etc': 'phd_civil',
            'Any Other Education Category': 'other',
        }
        occupation_map = {
            'Government Job': 'government_job',
            'Private MNC Job': 'private_mnc_job',
            'Self Employed (Own Practice)': 'self_employed',
            'Own Business': 'own_business',
            'Job + Business': 'job_business',
            'Free Lancing': 'free_lancing',
            'Student (Studies Running)': 'student',
            'Searching Job': 'searching_job',
            'Home Works (ghar-kaam)': 'home_works',
        }
        shani_map = {
            'Yes (Shani)': 'yes_shani',
            'Yes (Mangal)': 'yes_mangal',
            'No': 'no',
            "Don't Know": 'dont_know',
            "We Don't Believe": 'dont_believe',
        }
        nadi_map = {
            'Aadhya Nadi': 'aadhya',
            'Madhya Nadi': 'madhya',
            'Antya Nadi': 'antya',
            'I Dont Know': 'dont_know',
            "We Don't Believe": 'dont_believe',
        }
        residence_area_map = {
            'Gujarat Region (North or Central or South)': 'gujarat',
            'Saurashtra Region': 'saurashtra',
            'Kachchh Region': 'kachchh',
            'Mumbai & Maharashtra Region': 'mumbai_maharashtra',
            'Rest of Indian Region (except Gujarat & Maharashtra)': 'rest_of_india',
            'NRI (Any Visa)': 'nri',
        }
        alcohol_map = {
            'Yes': 'yes',
            'No': 'no',
        }
        smoke_map = {
            'Yes': 'yes',
            'No': 'no',
        }
        obj = BhudevSammelanRegistration(
            candidate_name=request.POST.get('name'),
            candidate_gender=gender_map.get(request.POST.get('gender'), ''),
            registrant_relation=request.POST.get('who'),
            registrant_mobile=request.POST.get('regMobile'),
            candidate_current_city=request.POST.get('city'),
            dob=request.POST.get('dob'),
            marital_status=request.POST.get('marital'),
            birth_time=request.POST.get('tob'),
            birth_place=request.POST.get('birthPlace'),
            residence_area_category=request.POST.get('resCat'),
            current_country=request.POST.get('country'),
            visa_status=visa_map.get(request.POST.get('visa'), ''),
            height=request.POST.get('height'),
            weight=request.POST.get('weight'),
            education_category=education_map.get(request.POST.get('education'), ''),
            education_detail=request.POST.get('educationDetail'),
            occupation_category=occupation_map.get(request.POST.get('occupationCat'), ''),
            occupation_details=request.POST.get('occupationDetails'),
            salary=request.POST.get('salary'),
            shani_mangal=shani_map.get(request.POST.get('shani'), ''),
            hobbies=request.POST.get('hobbies'),
            nadi=nadi_map.get(request.POST.get('nadi'), ''),
            email=request.POST.get('email'),
            whatsapp_number=request.POST.get('whatsapp'),
            father_name=request.POST.get('father'),
            mother_name=request.POST.get('mother'),
            father_mobile=request.POST.get('fatherWp'),
            mother_mobile=request.POST.get('motherWp'),
            type_of_brahmin=request.POST.get('caste'),
            gotra=request.POST.get('gotra'),
            kuldevi=request.POST.get('kuldevi'),
            disability=request.POST.get('disability'),
            siblings=request.POST.get('siblings'),
            eating_habbits=request.POST.get('eating_habbits'),
            alcohol=alcohol_map.get(request.POST.get('alcohol'), ''),
            smoke=smoke_map.get(request.POST.get('smoke'), ''),
            other_habbit=request.POST.get('other_habbit'),
            legal_case=request.POST.get('legal_case'),
            partner_location=request.POST.get('locChoice'),
            partner_age_bracket=request.POST.get('ageGap'),
            partner_education=request.POST.get('eduChoice'),
            other_specific_choice=request.POST.get('otherChoice'),
            photograph=request.FILES.get('photo'),
            declaration=declaration_map.get(request.POST.get('declaration'), ''),
        )
        obj.save()
        return render(request, 'biodata/bhudev_sammelan_form_success.html')
    # For GET or any other method, render the form
    return render(request, 'biodata/bhudev_sammelan_form.html')

# Restore judge_application view for URL resolution


def garba_pass_registration_view(request):
    if request.method == 'POST':
        # Only Garba Pass is available, so process accordingly
        full_name = request.POST.get('full_name', '').strip()
        date_of_birth = request.POST.get('date_of_birth', '').strip()
        residence_city = request.POST.get('residence_city', '').strip()
        whatsapp_number = request.POST.get('whatsapp_number', '').strip()
        try:
            quantity = int(request.POST.get('garbaPassQty', '1'))
        except (ValueError, TypeError):
            quantity = 1
        subtotal = 50 * quantity
        passes = [{
            'type': 'Garba Pass',
            'quantity': quantity,
            'amount': subtotal
        }]
        payment_screenshot = request.FILES.get('payment_screenshot')

        registration = GarbaPassRegistration(
            full_name=full_name,
            date_of_birth=date_of_birth,
            residence_city=residence_city,
            whatsapp_number=whatsapp_number,
            passes=passes,
            subtotal=subtotal,
            payment_screenshot=payment_screenshot
        )
        try:
            registration.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'redirect_url': '/garba-confirmation/'})
            else:
                return render(request, 'biodata/garba_confirmation.html')
        except Exception as e:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': str(e)}, status=400)
            else:
                return render(request, 'biodata/garba_form.html', {'form': None, 'error': str(e)})
    else:
        form = GarbaPassRegistrationForm()
    return render(request, 'biodata/garba_form.html', {'form': form})


def birthday_form_view(request):
    # Render the static birthday form page
    return render(request, 'biodata/birthdayform.html')


def birthday_confirmation(request):
    # Simple confirmation page after successful birthday form submission
    return render(request, 'biodata/birthday_confirmation.html')


@csrf_exempt
def submit_birthday(request):
    # Accept JSON POST from the birthday form JS
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Only POST allowed'}, status=405)
    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        # Sometimes hosted environments or proxies submit form-encoded data instead of JSON.
        # Attempt a safe fallback to request.POST if available, otherwise return a clearer error.
        logging.getLogger(__name__).warning('submit_birthday: JSON parse failed; trying request.POST fallback; content_type=%s', getattr(request, 'content_type', None))
        if request.POST:
            # Build a small dict from POST values using the same keys we expect from the frontend
            data = {
                'candidateName': request.POST.get('candidateName') or request.POST.get('candidateName[]') or request.POST.get('candidate_name'),
                'birthDate': request.POST.get('birthDate') or request.POST.get('birth_date'),
                'mobile1': request.POST.get('mobile1'),
                'mobile2': request.POST.get('mobile2'),
                'mobile3': request.POST.get('mobile3'),
                'cityName': request.POST.get('cityName') or request.POST.get('city'),
                # Removed website and dataEntryPerson
            }
        else:
            # No POST data; log a short preview of the raw body for debugging and return an informative error
            raw_preview = request.body.decode('utf-8', errors='replace')[:2000]
            logging.getLogger(__name__).error('submit_birthday: invalid/empty request body. content_type=%s body_preview=%s', getattr(request, 'content_type', None), raw_preview)
            return JsonResponse({'success': False, 'error': 'Invalid JSON or empty request body', 'content_type': getattr(request, 'content_type', None)}, status=400)

    # Minimal validation
    name = data.get('candidateName', '').strip()
    birth_date = data.get('birthDate', '').strip()
    mobile1 = data.get('mobile1', '').strip()
    # Removed website and dataEntryPerson
    city = data.get('cityName', '').strip() or None
    mobile2 = data.get('mobile2', '').strip() or None
    mobile3 = data.get('mobile3', '').strip() or None

    if not name or not birth_date or not mobile1:
        return JsonResponse({'success': False, 'error': 'Missing required fields'}, status=400)

    # Save to DB
    try:
        import logging
        from datetime import datetime
        logger = logging.getLogger(__name__)
        logger.debug('submit_birthday payload: %s', data)

        # Try parsing birth_date in several common formats
        parsed_date = None
        for fmt in ('%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y', '%m/%d/%Y'):
            try:
                parsed_date = datetime.strptime(birth_date, fmt).date()
                break
            except Exception:
                continue

        if parsed_date is None:
            # Try to trim time portion if included (ISO with time)
            try:
                parsed_date = datetime.fromisoformat(birth_date).date()
            except Exception:
                logger.error('Invalid date format for birth_date: %s', birth_date)
                return JsonResponse({'success': False, 'error': 'Invalid birthDate format. Use YYYY-MM-DD or DD-MM-YYYY.'}, status=400)

        from .models import BirthdayFormSubmission
        obj = BirthdayFormSubmission.objects.create(
            candidate_name=name,
            birth_date=parsed_date,
            mobile_1=mobile1,
            mobile_2=mobile2,
            mobile_3=mobile3,
            city=city,
            # Removed website and data_entry_person
        )
        logger.info('Created BirthdayFormSubmission id=%s for %s', obj.id, name)
        # Provide a redirect URL for the frontend to navigate to a confirmation page
        try:
            redirect_url = reverse('birthday_confirmation')
        except Exception:
            redirect_url = '/birthday-confirmation/'
        return JsonResponse({'success': True, 'id': obj.id, 'redirect_url': redirect_url})
    except Exception as e:
        import logging
        logging.exception('Error saving birthday submission')
        return JsonResponse({'success': False, 'error': 'Server error saving submission'}, status=500)


    boy_name = (data.get('boyName') or '').strip()
    girl_name = (data.get('girlName') or '').strip()
    # Added boy_birth_date per request; keep girl_birth_date as well
    boy_birth_date = (data.get('boyBirthDate') or '').strip()
    girl_birth_date = (data.get('girlBirthDate') or '').strip()
    boy_city = (data.get('boyCity') or '').strip()
    girl_city = (data.get('girlCity') or '').strip()
    who_is_filling = (data.get('whoIsFilling') or '').strip()
    mobile_number = (data.get('mobileNumber') or '').strip()
    whatsapp_number = (data.get('whatsappNumber') or '').strip()
    relationship_status = (data.get('relationshipStatus') or '').strip()
    function_date_val = (data.get('functionDate') or '').strip()
    message = (data.get('message') or '').strip()

    # Save to DB
    try:
        from .models import StorySubmission

        # Helper to parse additional dates
        def parse_optional_date(val):
            if not val:
                return None
            from datetime import datetime
            for fmt in ('%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y'):
                try:
                    return datetime.strptime(val, fmt).date()
                except Exception:
                    continue
            return None

        # Create the object first without the file to isolate file storage errors.
        obj = StorySubmission.objects.create(
            boy_name=boy_name or None,
            girl_name=girl_name or None,
            boy_birth_date=parse_optional_date(boy_birth_date),
            girl_birth_date=parse_optional_date(girl_birth_date),
            boy_city=boy_city or None,
            girl_city=girl_city or None,
            who_is_filling=who_is_filling or None,
            mobile_number=mobile_number or None,
            whatsapp_number=whatsapp_number or None,
            relationship_status=relationship_status or None,
            function_date=parse_optional_date(function_date_val),
            message=message or None,
        )
        # Log creation to help debugging (use couple names instead of removed title)
        logging.getLogger(__name__).info('StorySubmission created id=%s boy=%s girl=%s', obj.id, obj.boy_name, obj.girl_name)

        # Attach image if provided, but handle storage errors separately so we don't return 500
        # Frontend sends file input named 'photos' (may be multi-file). Accept either 'image' or 'photos'.
        if not image_file:
            # try multiple files under 'photos'
            if request.FILES:
                files = request.FILES.getlist('photos')
                if files:
                    image_file = files[0]

        if image_file:
            try:
                obj.image = image_file
                obj.save()
            except Exception as img_err:
                logging.getLogger(__name__).exception('Failed saving image for StorySubmission id=%s', obj.id)
                # Return error but keep the created record so data is not lost
                try:
                    exc_text = str(img_err)
                    exc_type = type(img_err).__name__
                except Exception:
                    exc_text = 'UnknownImageSaveError'
                    exc_type = 'UnknownError'
                return JsonResponse({'success': False, 'error': 'Image save failed', 'exception': exc_text, 'exception_type': exc_type, 'id': obj.id}, status=500)

        # Provide a thank-you page URL. If the client is sending an AJAX request, return JSON
        # including the redirect_url. If it's a normal form POST, perform a server-side redirect.
        try:
            redirect_url = reverse('happy_stories_thanks')
        except Exception:
            redirect_url = '/happy-stories/thanks/'

        # Return JSON including the redirect_url so the frontend (fetch/ajax or normal form
        # submission) can handle client-side navigation. Frontend should use the returned
        # `redirect_url` (e.g. window.location = redirect_url) to go to the thank-you page.
        return JsonResponse({'success': True, 'id': obj.id, 'redirect_url': redirect_url})
    except Exception as e:
        # Log full traceback and return the exception text in JSON to help debugging during development
        logger = logging.getLogger(__name__)
        logger.exception('Error saving story submission')
        # Include exception details in the response (helpful while debugging locally)
        try:
            exc_text = str(e)
            exc_type = type(e).__name__
        except Exception:
            exc_text = 'Unknown error'
            exc_type = 'UnknownError'
        return JsonResponse({'success': False, 'error': 'Server error saving submission', 'exception': exc_text, 'exception_type': exc_type}, status=500)


def garba_confirmation(request):
    return render(request, 'biodata/garba_confirmation.html')


def happy_stories_view(request):
    """Render the Happy Stories submission page."""
    return render(request, 'biodata/happy_stories.html')


def happy_stories_thanks_view(request):
    """Render a small thank-you page after story submission."""
    return render(request, 'biodata/happy_stories_thanks.html')

def courier_booklet_35th_view(request):
    """Handle the 35th Courier Booklet booking page (separate model/form)."""
    from .forms import CourierBooklet35thForm
    from django.contrib import messages
    from .models import CourierBooklet35thBooking
    from django.db import transaction
    
    if request.method == 'POST':
        print("POST request received for 35th Courier Booklet form.")
        form = CourierBooklet35thForm(request.POST, request.FILES)
        print(f"Form data: {request.POST}, Files: {request.FILES}")
        if form.is_valid():
            try:
                # Use atomic transaction to ensure commit
                with transaction.atomic():
                    booking = form.save()
                    print(f"CourierBooklet35thBooking saved: {booking}")
                    print(f"Saved object ID: {booking.id}")
                
                # Verify save after transaction commits
                verify = CourierBooklet35thBooking.objects.filter(id=booking.id).first()
                print(f"Verification query result after transaction: {verify}")
                
                if verify:
                    print("SUCCESS: Object is in database!")
                else:
                    print("ERROR: Object not found after transaction!")
                    
                return redirect('35th_curier_booklet_success')
                
            except Exception as e:
                print(f"Exception during save: {e}")
                import traceback
                traceback.print_exc()
                messages.error(request, 'An error occurred while saving your booking. Please try again.')
        else:
            print(f"CourierBooklet35thForm errors: {form.errors}")
            messages.error(request, 'Please correct the errors below and try again.')
    else:
        form = CourierBooklet35thForm()
    
    return render(request, 'biodata/35th_Courier_Booklet.html', {'form': form})

# ...existing code...
def courier_booklet_35th_success(request):
    return render(request, 'biodata/35th_Curier_booklet_success.html')

def booklet_camp_adv_booking_view(request):
    """Handle the Booklet Camp Advanced Booking form."""
    if request.method == 'POST':
        print("[DEBUG] POST request received for booklet_camp_adv_booking_view")
        data = request.POST.copy()
        data['name'] = data.get('fullName', '')
        data['phone'] = data.get('mobileNumber', '')
        import re
        date_input = data.get('dateOfBirth', '')
        date_parsed = ''
        match = re.match(r'^(\d{2})[-/](\d{2})[-/](\d{4})$', date_input)
        if match:
            day, month, year = match.groups()
            date_parsed = f"{year}-{month}-{day}"
        data['booking_date'] = date_parsed
        data['city'] = data.get('city', '')
        data['book'] = data.get('book', '')
        print(f"[DEBUG] Data sent to form: {data}")
        form = BookletCampAdvBookingForm(data)
        print(f"[DEBUG] Form valid: {form.is_valid()}")
        if not form.is_valid():
            print(f"[DEBUG] Form errors: {form.errors}")
        if form.is_valid():
            form.save()
            print("[DEBUG] Form saved successfully, redirecting to confirmation.")
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                from django.urls import reverse
                return JsonResponse({'success': True, 'redirect_url': reverse('booklet_camp_adv_booking_confirmation')})
            else:
                return redirect('booklet_camp_adv_booking_confirmation')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
            else:
                return render(request, 'biodata/booklet_camp_adv_booking.html', {'form': form, 'success': False})
    else:
        form = BookletCampAdvBookingForm()
    return render(request, 'biodata/booklet_camp_adv_booking.html', {'form': form})

def booklet_camp_adv_booking_confirmation(request):
    return render(request, 'biodata/booklet_camp_adv_booking_confirmation.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def bncf_application_view(request):
    if request.method == 'POST':
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            import json, logging
            try:
                data = json.loads(request.body)
                obj = BncBnfApplication.objects.create(
                    full_name=data.get('fullName', ''),
                    gender=data.get('gender', ''),
                    date_of_birth=data.get('dob', ''),
                    marriage_status=data.get('maritalStatus', ''),
                    whatsapp_number=data.get('whatsapp', ''),
                    phone_number=data.get('phone', ''),
                    education=data.get('education', ''),
                    occupation=data.get('occupation', ''),
                    current_city=data.get('city', ''),
                    area_name=data.get('area', ''),
                    home_address=data.get('address', ''),
                )
                return JsonResponse({'success': True, 'id': obj.id})
            except Exception as e:
                logging.error(f"BNCF Application form submission error: {e}")
                return JsonResponse({'success': False, 'error': str(e)}, status=500)
        else:
            form = BncBnfApplicationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'biodata/bncf_success.html')
    else:
        form = BncBnfApplicationForm()
    return render(request, 'biodata/bncf_form.html', {'form': form})
from .forms_business_directory import BusinessDirectoryForm
from .models_business_directory import BusinessDirectoryEntry
def business_directory(request):
    if request.method == 'POST':
        form = BusinessDirectoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'biodata/business_directory_confirmation.html')
        else:
            print('BusinessDirectoryForm errors:', form.errors)  # Debug print to console
            return render(request, 'biodata/bussiness_directory.html', {
                'form': form,
                'success': False
            })
    else:
        form = BusinessDirectoryForm()
    return render(request, 'biodata/bussiness_directory.html', {'form': form})
def technical_support_confirmation(request):
    return render(request, 'biodata/technical_support_confirmation.html')
from django.shortcuts import render, redirect, get_object_or_404
from .forms_astrology import AstrologyForm

from .form_spot import AdvanceBookletBookingForm
from .forms_booklet_camp_adv import BookletCampAdvBookingForm

from django.http import FileResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from biodata.forms_mega_correction import MegaBookletCorrectionForm
from .models import CandidateBiodata, AdvancePassBooking, AdvanceBookletBooking, StageRegistration, MegaBookletCorrectionRequest
from biodata.views_weasyprint import generate_pdf
from .forms_stage_registration import StageRegistrationForm

# Removed import of CandidateBiodataForm as it does not exist in biodata/forms.py
from .forms_advance_pass import AdvancePassBookingForm
from .forms_advance_booklet import AdvanceBookletBookingForm
from django.core.mail import EmailMessage
from django.conf import settings
import logging
from django.shortcuts import render, redirect
from .forms_zoom import ZoomRegistrationForm

logger = logging.getLogger(__name__)

from django.http import JsonResponse

def mega_booklet_correction_request(request):
    if request.method == 'POST':
        form = MegaBookletCorrectionForm(request.POST, request.FILES)
        if form.is_valid():
            correction_request = form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'requestId': correction_request.id})
            else:
                return redirect('mega_booklet_correction_confirmation', request_id=correction_request.id)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = form.errors.as_json()
                return JsonResponse({'success': False, 'message': 'Form validation failed', 'errors': errors})
    else:
        form = MegaBookletCorrectionForm()
    return render(request, 'biodata/mega_booklet_data_correction_form.html', {'form': form})

def mega_booklet_correction_confirmation(request, request_id):
    from django.shortcuts import get_object_or_404
    correction_request = get_object_or_404(MegaBookletCorrectionRequest, id=request_id)
    return render(request, 'biodata/mega_booklet_correction_confirmation.html', {'correction_request': correction_request})



def home_page(request):
    from .forms import CandidateBiodataForm
    if request.method == 'POST':
        form = CandidateBiodataForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            pdf_buffer = generate_pdf(instance)
            # You can save or email the PDF as needed here
            # Redirect after POST to avoid resubmission on refresh
            return redirect('confirmation', candidate_id=instance.id)
        else:
            # Form invalid, render home page with form and errors
            # Add a flag to indicate form errors for template use
            return render(request, 'biodata/home.html', {'form': form, 'form_errors': True})
    else:
        form = CandidateBiodataForm()
    return render(request, 'biodata/home.html', {'form': form})

from .models_astrology import AstrologyFormSubmission

def astrology_form_view(request):
    if request.method == 'POST':
        form = AstrologyForm(request.POST)
        if form.is_valid():
            # Save form data to AstrologyFormSubmission model
            data = form.cleaned_data
            submission = AstrologyFormSubmission(
                name=data['name'],
                whatsapp=data['whatsapp'],
                city=data['city'],
                candidateName=data['candidateName'],
                candidateDOB=data['candidateDOB'],
                candidateBirthTime=data['candidateBirthTime'],
                candidateBirthPlace=data['candidateBirthPlace'],
                description=data['description']
            )
            submission.save()
            confirmation_message = "Your query form has been submitted"
            return render(request, 'biodata/Astroconfirmation_page.html', {'form': form, 'confirmation_message': confirmation_message})
    else:
        form = AstrologyForm()
    return render(request, 'biodata/astrology_form.html', {'form': form})


def stage_registration(request):
    import logging
    logger = logging.getLogger(__name__)
    if request.method == 'POST':
        logger.info("Received POST request in stage_registration view")
        form = StageRegistrationForm(request.POST, request.FILES)
        logger.info(f"POST data received: {request.POST}")
        logger.info(f"FILES data received: {request.FILES}")
        if form.is_valid():
            logger.info("StageRegistrationForm is valid")
            instance = form.save()
            logger.info(f"Saved instance with id: {instance.id}")
            # Additional debug info
            logger.info(f"Saved instance data: {instance.__dict__}")
            # Redirect to confirmation page after successful submission
            return redirect('stage_registration_confirmation', registration_id=instance.id)
        else:
            logger.warning(f"StageRegistrationForm is invalid: {form.errors}")
            logger.warning(f"Form errors details: {form.errors.as_json()}")
            return render(request, 'biodata/stage_registration_form.html', {'form': form, 'form_errors': form.errors})
    else:
        form = StageRegistrationForm()
    return render(request, 'biodata/stage_registration_form.html', {'form': form})


def stage_registration_confirmation(request, registration_id):
    registration = get_object_or_404(StageRegistration, id=registration_id)
    return render(request, 'biodata/stage_registration_confirmation.html', {'stage_registration': registration})




import threading

def send_email_async(email):
    try:
        email.send(fail_silently=False)
    except Exception as e:
        logger.error(f"Failed to send email asynchronously: {e}")

def advance_pass_booking(request):
    if request.method == 'POST':
        form = AdvancePassBookingForm(request.POST, request.FILES)

        if form.is_valid():
            entry_token_qty = int(form.cleaned.data.get('entry_token_quantity', 0))
            unlimited_buffet_qty = int(form.cleaned.data.get('unlimited_buffet_quantity', 0))

            total_amount = (entry_token_qty * 20 + unlimited_buffet_qty * 200)

            existing_booking = AdvancePassBooking.objects.filter(
                email=form.cleaned.data['email'],
                entry_token_quantity=entry_token_qty,
                unlimited_buffet_quantity=unlimited_buffet_qty,
            ).first()

            if existing_booking:
                error_message = "A booking with the same details already exists. Duplicate submission is not allowed."
                return render(request, 'biodata/advance_pass_booking.html', {'form': form, 'error_message': error_message})

            advance_pass_booking = AdvancePassBooking(
                name=form.cleaned.data['name'],
                city=form.cleaned.data['city'],
                whatsapp_number=form.cleaned.data['whatsapp_number'],
                email=form.cleaned.data['email'],
                entry_token_quantity=entry_token_qty,
                unlimited_buffet_quantity=unlimited_buffet_qty,
                payment_screenshot=form.cleaned.data['payment_screenshot'],
                total_amount=total_amount,
            )
            advance_pass_booking.save()

            # Send confirmation email asynchronously
            email_subject = 'Advance Pass Booking Confirmation'
            email_body = f"Dear {form.cleaned.data['name']},\n\nThank you for your advance pass booking.\n\nDetails:\n"
            if entry_token_qty > 0:
                email_body += f"Entry Token Pass x {entry_token_qty}\n"
            if unlimited_buffet_qty > 0:
                email_body += f"Unlimited Buffet Lunch x {unlimited_buffet_qty}\n"
            email_body += f"Total Amount: ₹{total_amount}\n\nThis booking Confirmation is valid only if your Payment is valid and if we have duly received your Payment as per your information given to us.\n\nRegards,\nEvent Team"
            print(f"Sending email from: {settings.DEFAULT_FROM_EMAIL} to: {form.cleaned.data['email']}")
            if getattr(settings, 'EMAIL_SEND_AUTOMATIC', True):
                email = EmailMessage(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [form.cleaned.data['email']],
                )
                threading.Thread(target=send_email_async, args=(email,)).start()
            else:
                logger.info(f"EMAIL_SEND_AUTOMATIC is False: skipping advance_pass_booking confirmation email to {form.cleaned.data.get('email')}")

            return render(request, 'biodata/advance_pass_booking_success.html', {'form': form, 'total_amount': total_amount})
        else:
            return render(request, 'biodata/advance_pass_booking.html', {'form': form})
    else:
        form = AdvancePassBookingForm()
    return render(request, 'biodata/advance_pass_booking.html', {'form': form})

from django.views.decorators.csrf import csrf_exempt

import logging
from django.views.decorators.csrf import csrf_exempt
import io
import os
import zipfile
import pandas as pd
from django.http import HttpResponse
from django.conf import settings
from .models import AdvanceBookletBooking
import threading
from django.core.mail import EmailMessage

@csrf_exempt
def advance_booklet_booking(request):
    logger.info(f"advance_booklet_booking called with method: {request.method}")
    if request.method == 'POST':
        form = AdvanceBookletBookingForm(request.POST, request.FILES)
        if form.is_valid():
            logger.info("Form is valid")
            total_amount = form.cleaned.data.get('total_amount', 0)

            advance_booklet_booking = form.save(commit=False)
            advance_booklet_booking.total_amount = total_amount
            advance_booklet_booking.with_courier = True
            advance_booklet_booking.save()

            # Send confirmation email asynchronously
            email_subject = 'Advance Booklet Booking Confirmation'
            email_body = f"Dear {form.cleaned.data['name']},\n\nThank you for your advance booklet booking.\n\nDetails:\n"
            if form.cleaned.data.get('girls_booklet_with'):
                email_body += "Girls Biodata Booklet (With Courier)\n"
            if form.cleaned.data.get('boys_booklet_with'):
                email_body += "Boys Biodata Booklet (With Courier)\n"
            email_body += f"Courier Address: {form.cleaned.data.get('courier_address')}\n"
            email_body += f"Total Amount: ₹{total_amount}\n\nThis booking Confirmation is valid only if your Payment is valid and if we have duly received your Payment as per your information given to us.\n\nRegards,\nEvent Team"
            print(f"Sending email from: {settings.DEFAULT_FROM_EMAIL} to: {form.cleaned.data['email']}")
            if getattr(settings, 'EMAIL_SEND_AUTOMATIC', True):
                email = EmailMessage(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [form.cleaned.data['email']],
                )
                threading.Thread(target=send_email_async, args=(email,)).start()
            else:
                logger.info(f"EMAIL_SEND_AUTOMATIC is False: skipping advance_booklet_booking confirmation email to {form.cleaned.data.get('email')}")

            logger.info("Redirecting to confirmation page")
            return redirect('advance_booklet_booking_confirmation', booking_id=advance_booklet_booking.id)
        else:
            logger.info("Form is invalid")
            # --- DEBUG CODE START ---
            print("Form errors:", form.errors)
            print("Non-field errors:", form.non_field_errors())
            logger.error(f"Form errors: {form.errors}")
            logger.error(f"Non-field errors: {form.non_field_errors()}")
            print("POST data:", request.POST)
            print("FILES data:", request.FILES)
            # --- DEBUG CODE END ---
            return render(request, 'biodata/Advance_booklet_booking.html', {'form': form})
    else:
        logger.info("GET request, rendering form")
        form = AdvanceBookletBookingForm()
    return render(request, 'biodata/Advance_booklet_booking.html', {'form': form})

def export_booklet_booking_and_images(request):
    bookings = AdvanceBookletBooking.objects.all()

    data = []
    for booking in bookings:
        data.append({
            'Name': booking.name,
            'City': booking.city,
            'Whatsapp Number': booking.whatsapp_number,
            'Email': booking.email,
            'Girls Booklet With': booking.girls_booklet_with,
            'Boys Booklet With': booking.boys_booklet_with,
            'Courier Address': booking.courier_address,
            'Total Amount': booking.total_amount,
        })

    df = pd.DataFrame(data)

    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Bookings')
        workbook = writer.book
        worksheet = writer.sheets['Bookings']

        # Set column width for better image display
        worksheet.set_column('A:H', 20)

        # Start inserting images from row 1 (after header)
        row = 1
        for booking in bookings:
            if booking.payment_screenshot:
                image_path = os.path.join(settings.MEDIA_ROOT, booking.payment_screenshot.name)
                if os.path.exists(image_path):
                    # Insert image in the last column (I)
                    # Calculate cell position, e.g., 'I' + str(row+1)
                    cell_location = f'I{row + 1}'
                    # Insert image with scaling to fit cell
                    worksheet.insert_image(cell_location, image_path, {'x_scale': 0.5, 'y_scale': 0.5, 'object_position': 1})
            row += 1

        # Set header for image column
        worksheet.write('I1', 'Payment Screenshot')

    excel_buffer.seek(0)

    response = HttpResponse(excel_buffer.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=booklet_bookings_with_images.xlsx'
    return response

def biodata_form(request):
    # Deprecated: form handled in home_page now
    return redirect('home_page')

def download_biodata_pdf(request, candidate_id):
    instance = get_object_or_404(CandidateBiodata, id=candidate_id)
    try:
        pdf_buffer = generate_pdf(instance)
        pdf_buffer.seek(0)
        return FileResponse(pdf_buffer, as_attachment=True, filename='biodata.pdf')
    except FileNotFoundError:
        # Handle missing image file gracefully
        return HttpResponse("Error: Some image files are missing. Please contact support.", status=404)

from django.core.mail import EmailMessage
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def confirmation_page(request, candidate_id):
    candidate = get_object_or_404(CandidateBiodata, id=candidate_id)
    whatsapp_group_link = "https://chat.whatsapp.com/BltytlRjrZm1HWYvhley24"
    email_sent = True
    try:
        pdf_buffer = generate_pdf(candidate)
        pdf_buffer.seek(0)
        email = EmailMessage(
            subject='Your Biodata Submission Confirmation',
            body='Thank you for submitting your biodata. Please find the attached PDF.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[candidate.email],
        )
        email.attach('biodata.pdf', pdf_buffer.read(), 'application/pdf')
        email.send(fail_silently=False)
    except Exception as e:
        logger.error(f"Failed to send confirmation email to {candidate.email}: {e}")
        email_sent = False
        # Add detailed error message to context for debugging
        return render(request, 'biodata/confirmation.html', {
            'candidate': candidate,
            'whatsapp_group_link': whatsapp_group_link,
            'email_sent': email_sent,
            'error_message': str(e),
        })
    return render(request, 'biodata/confirmation.html', {'candidate': candidate, 'whatsapp_group_link': whatsapp_group_link, 'email_sent': email_sent})

def advance_booklet_booking_confirmation(request, booking_id):
    booking = get_object_or_404(AdvanceBookletBooking, id=booking_id)
    return render(request, 'biodata/advance_booklet_booking_success.html', {'booking': booking})

def confirmation_redirect(request):
    return HttpResponseRedirect(reverse('home_page'))

from .models import CandidateBiodata, GalleryImage

def gallery_page(request):
    # Query all gallery images from the database
    images = GalleryImage.objects.all()
    return render(request, 'biodata/gallery.html', {'images': images})

def contact_us_page(request):
    # Render the contact us page
    return render(request, 'biodata/contact_us.html')

def about_us_page(request):
    # Render the about us page
    return render(request, 'biodata/about_us.html')

def spot_advance_booklet_view(request):
    from .form_spot import AdvanceBookletBookingForm as SpotAdvanceBookletBookingForm
    if request.method == 'POST':
        form = SpotAdvanceBookletBookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save()
            return redirect('spot_advance_booklet_confirmation', booking_id=booking.id)
    else:
        form = SpotAdvanceBookletBookingForm()
    return render(request, 'biodata/spot_advance_booklet.html', {'form': form})

from .models import SpotAdvanceBookletBooking

def spot_advance_booklet_confirmation(request, booking_id):
    booking = get_object_or_404(SpotAdvanceBookletBooking, id=booking_id)
    return render(request, 'biodata/spot_advance_booklet_confirmation.html', {'booking': booking})


def register_view(request):
    if request.method == 'POST':
        form = ZoomRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('zoom_confirmation')
    else:
        form = ZoomRegistrationForm()
    return render(request, 'biodata/zoom_form.html', {'form': form})

def confirmation_view(request):
    return render(request, 'biodata/zoom_confirmation.html')

from .forms_technical_support import TechnicalSupportForm
from .models_technical_support import TechnicalSupportRequest, SupportAttachment
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import json

def technical_support(request):
    if request.method == 'POST':
        form = TechnicalSupportForm(request.POST, request.FILES)
        if form.is_valid():
            support_request = form.save()
            # Handle file attachments
            attachments = request.FILES.getlist('attachments')
            for file in attachments:
                SupportAttachment.objects.create(
                    support_request=support_request,
                    file=file,
                    filename=file.name
                )
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Your support request has been submitted successfully!',
                    'request_id': support_request.id
                })
            else:
                return redirect('technical_support_confirmation')
        else:
            print('Form validation errors:', form.errors)  # Print to console
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f'TechnicalSupportForm errors: {form.errors.as_json()}')
            errors = form.errors.as_json()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Form validation failed', 'errors': errors})
            else:
                messages.error(request, 'Form validation failed. Please check your inputs.')
    else:
        form = TechnicalSupportForm()
    return render(request, 'biodata/technical_support_form.html', {'form': form})
from .views_karmkand_directory import global_karmkand_directory

# The garba_form_view and submit_garba_form are redundant and conflict with garba_pass_registration_view
# Removing these to avoid confusion and conflicts

# def garba_form_view(request):
#     return render(request, 'biodata/garba_form.html')

# def submit_garba_form(request):
#     if request.method == 'POST':
#         # You can process and save form data here
#         return render(request, 'biodata/garba_success.html')
#     return redirect('garba_form')

from .forms_participant import ParticipantRegistrationForm
from .models import ParticipantRegistration

def participant_form_view(request):
    """Handle participant registration form submission"""
    if request.method == 'POST':
        # Handle AJAX request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            try:
                # Get form data
                first_name = request.POST.get('first_name', '').strip()
                last_name = request.POST.get('last_name', '').strip()
                email = request.POST.get('email', '').strip()
                phone_number = request.POST.get('phone_number', '').strip()
                events = request.POST.getlist('events[]')  # Get selected events
                payment_screenshot = request.FILES.get('payment_screenshot')
                
                # Validate required fields
                if not all([first_name, last_name, email, phone_number, payment_screenshot]):
                    return JsonResponse({
                        'success': False, 
                        'error': 'All fields are required.'
                    }, status=400)
                
                if not events:
                    return JsonResponse({
                        'success': False, 
                        'error': 'Please select at least one event.'
                    }, status=400)
                
                # Calculate subtotal
                subtotal = len(events) * 50
                
                # Create participant registration
                participant = ParticipantRegistration.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    events=events,
                    subtotal=subtotal,
                    payment_screenshot=payment_screenshot
                )
                
                return JsonResponse({
                    'success': True,
                    'message': 'Registration submitted successfully!',
                    'redirect_url': f'/participant-confirmation/{participant.id}/'
                })
                
            except Exception as e:
                logging.error(f"Participant form submission error: {e}")
                return JsonResponse({
                    'success': False, 
                    'error': 'An error occurred while processing your registration. Please try again.'
                }, status=500)
        
        # Handle regular form submission
        else:
            form = ParticipantRegistrationForm(request.POST, request.FILES)
            if form.is_valid():
                participant = form.save()
                return redirect('participant_confirmation', participant_id=participant.id)
            else:
                return render(request, 'biodata/participantForm.html', {'form': form})
    
    # Handle GET request
    else:
        form = ParticipantRegistrationForm()
    
    return render(request, 'biodata/participantForm.html', {'form': form})

def participant_confirmation(request, participant_id):
    """Display confirmation page after successful registration"""
    try:
        participant = ParticipantRegistration.objects.get(id=participant_id)
        return render(request, 'biodata/participant_success.html', {'participant': participant})
    except ParticipantRegistration.DoesNotExist:
        return render(request, 'biodata/participant_success.html', {'error': 'Registration not found.'})

def audience_registration_view(request):
    """Handle audience ticket registration form submission and display"""
    if request.method == 'POST':
        try:
            # Extract form data
            first_name = request.POST.get('first_name', '').strip()
            last_name = request.POST.get('last_name', '').strip()
            email = request.POST.get('email', '').strip()
            phone_number = request.POST.get('phone_number', '').strip()
            ticket_quantity = int(request.POST.get('ticket_quantity', '1'))
            total_amount = float(request.POST.get('total_amount', '50.00'))
            payment_screenshot = request.FILES.get('payment_screenshot')

            # Validate ticket quantity and amount
            if ticket_quantity < 1 or ticket_quantity > 10:
                raise ValueError("Invalid ticket quantity")
            
            expected_amount = ticket_quantity * 50.00
            if abs(total_amount - expected_amount) > 0.01:
                raise ValueError("Total amount doesn't match ticket quantity")

            # Create audience registration
            registration = AudienceRegistration(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                ticket_quantity=ticket_quantity,
                total_amount=total_amount,
                payment_screenshot=payment_screenshot
            )
            registration.save()

            # Return success response
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True, 
                    'message': 'Registration successful!',
                    'redirect_url': '/audience-confirmation/'
                })
            else:
                return redirect('audience_confirmation')

        except ValueError as ve:
            error_msg = str(ve)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': error_msg}, status=400)
            else:
                form = AudienceRegistrationForm()
                return render(request, 'biodata/audience.html', {'form': form, 'error': error_msg})
        
        except Exception as e:
            error_msg = f"Registration failed: {str(e)}"
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': error_msg}, status=500)
            else:
                form = AudienceRegistrationForm()
                return render(request, 'biodata/audience.html', {'form': form, 'error': error_msg})
    
    else:
        form = AudienceRegistrationForm()
        return render(request, 'biodata/audience.html', {'form': form})

def audience_confirmation(request):
    """Display confirmation page after successful audience registration"""
    return render(request, 'biodata/audience_confirmation.html')


# 34th Sammelan Payment Form View
from .models import SammelanPaymentForm
from .forms import SammelanPaymentFormForm
from django.contrib import messages

def sammelan_payment_form_view(request):
    """Handle 34th Sammelan payment form submission"""
    if request.method == 'POST':
        form = SammelanPaymentFormForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect('sammelan_payment_confirmation', payment_id=instance.id)
        else:
            return render(request, 'biodata/34th_sammelean_payment.html', {'form': form})
    else:
        form = SammelanPaymentFormForm()
        return render(request, 'biodata/34th_sammelean_payment.html', {'form': form})

def sammelan_payment_confirmation(request, payment_id):
    """Display confirmation page after successful payment submission"""
    from django.shortcuts import get_object_or_404
    payment = get_object_or_404(SammelanPaymentForm, id=payment_id)
    return render(request, 'biodata/sammelan_payment_confirmation.html', {'payment': payment})

def sammelan_payment_view(request):
    if request.method == 'POST':
        form = SammelanPaymentFormForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Payment details submitted successfully!')
            return render(request, 'biodata/bhudev_sammelan_form_success.html', {'candidate_name': form.cleaned.data.get('name')})
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SammelanPaymentFormForm()
    return render(request, 'biodata/34th_sammelean_payment.html', {'form': form})

from .forms import BookletLibraryForm
from django.contrib import messages
from django.shortcuts import redirect
from .models import BookletLibrarySubmission

def booklet_library_view(request):
    """Display and process the Booklet Library form"""
    if request.method == 'POST':
        form = BookletLibraryForm(request.POST)
        if form.is_valid():
            submission = form.save()
            return redirect('booklet_library_confirmation', pk=submission.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'biodata/Booklet_Library_.html', {'form': form})
    else:
        form = BookletLibraryForm()
    return render(request, 'biodata/Booklet_Library_.html', {'form': form})

def booklet_library_confirmation(request, pk):
    """Display the confirmation page after successful form submission"""
    try:
        submission = BookletLibrarySubmission.objects.get(pk=pk)
        return render(request, 'biodata/booklet_library_confirmation.html', {'submission': submission})
    except BookletLibrarySubmission.DoesNotExist:
        messages.error(request, 'Submission not found.')
        return redirect('booklet_library')

from .forms import PhysicalFormForm
from .models import PhysicalForm

def physical_form_view(request):
    errors = None
    if request.method == 'POST':
        form = PhysicalFormForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            from django.http import HttpResponseRedirect
            return HttpResponseRedirect('/physical-form-success/')
        else:
            errors = form.errors
    else:
        form = PhysicalFormForm()
    return render(request, 'biodata/physical_form.html', {'form': form, 'errors': errors})

def physical_form_success_view(request):
    return render(request, 'biodata/physical_form_success.html')
