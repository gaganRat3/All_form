import sys
import logging
import re
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date
from .forms_karmkand_directory import GlobalKarmkandDirectoryForm
from .models_karmkand_directory import GlobalKarmkandDirectoryEntry, KarmkandiMaharajDetails, LaghuRudraYajmanRegistration, ShivMandirShivalayInfo


def global_karmkand_directory(request):
    logger = logging.getLogger(__name__)
    def debug_log(msg):
        print(f"[GLOBAL_KARMKAND_DEBUG] {msg}", file=sys.stderr)
    if request.method == 'POST':
        logger.info('Received POST request for Global Karmkand Directory')
        debug_log('Received POST request for Global Karmkand Directory')
        try:
            # Map frontend field names to model fields
            post = request.POST.copy()
            files = request.FILES

            debug_log(f"POST data: {dict(post)}")
            debug_log(f"FILES data: {files}")

            # Handle checkboxes (arrays)
            brahman_activities = request.POST.getlist('brahman_activities')
            service_level = request.POST.getlist('serviceLevel')
            employment_status = request.POST.getlist('employmentStatus')

            debug_log(f"brahman_activities: {brahman_activities}")
            debug_log(f"service_level: {service_level}")
            debug_log(f"employment_status: {employment_status}")

            entry = GlobalKarmkandDirectoryEntry(
                name=post.get('name', ''),
                dob=post.get('dob', ''),
                location=post.get('location', ''),
                phone1=post.get('phone1', ''),
                phone2=post.get('phone2', ''),
                brahman_activities=','.join(brahman_activities),
                experience_years=post.get('experience_years', post.get('experience', 0)),
                other_skills=post.get('other_skills', post.get('skills', '')),
                service_level=','.join(service_level),
                employment_status=','.join(employment_status),
                terms_agreed=bool(post.get('terms_agreed', False)),
            )
            debug_log(f"Prepared entry: {entry}")
            # Handle file uploads
            if 'photo' in files:
                entry.photo = files['photo']
                debug_log(f"Photo file received: {files['photo']}")
            if 'visitingCard' in files:
                entry.visiting_card = files['visitingCard']
                debug_log(f"Visiting card file received: {files['visitingCard']}")
            entry.save()
            debug_log(f"Entry saved successfully: {entry}")
            logger.info(f"Saved entry: {entry}")
            return render(request, 'biodata/global_karmkand_confirmation.html', {'success': True})
        except Exception as e:
            logger.error(f"Error saving GlobalKarmkandDirectoryEntry: {e}")
            debug_log(f"Error saving entry: {e}")
            return render(request, 'biodata/global_karmkand_directory.html', {'form': None, 'success': False, 'error': str(e)})
    else:
        form = GlobalKarmkandDirectoryForm()
    return render(request, 'biodata/global_karmkand_directory.html', {'form': form})


def karmkandi_maharaj_details_form_view(request):
    if request.method == 'POST':
        maharaj_name = (request.POST.get('maharaj_name') or '').strip()
        mobile_number = (request.POST.get('mobile_number') or '').strip()
        dob_value = request.POST.get('date_of_birth')
        experience_value = request.POST.get('laghurudra_experience')
        residence_city = (request.POST.get('residence_city') or '').strip()

        try:
            if not maharaj_name or not residence_city:
                raise ValueError('Please enter name and city.')
            if not re.fullmatch(r'\d{10}', mobile_number):
                raise ValueError('Please enter a valid 10-digit mobile number.')

            date_of_birth = parse_date(dob_value)
            if not date_of_birth:
                raise ValueError('Please select a valid date of birth.')

            laghurudra_experience = int(experience_value or 0)
            if laghurudra_experience < 0:
                raise ValueError('Experience cannot be negative.')

            KarmkandiMaharajDetails.objects.create(
                maharaj_name=maharaj_name,
                mobile_number=mobile_number,
                date_of_birth=date_of_birth,
                laghurudra_experience=laghurudra_experience,
                residence_city=residence_city,
            )
            return redirect('karmkandi_maharaj_details_success')
        except ValueError as exc:
            return render(
                request,
                'biodata/Karmkandi_Maharaj_Details_Form.html',
                {'error': str(exc), 'form_data': request.POST}
            )
        except Exception as exc:
            return render(
                request,
                'biodata/Karmkandi_Maharaj_Details_Form.html',
                {'error': 'Something went wrong while saving your form. Please try again.', 'form_data': request.POST}
            )

    return render(request, 'biodata/Karmkandi_Maharaj_Details_Form.html')


def karmkandi_maharaj_details_success(request):
    return render(request, 'biodata/karmkandi_maharaj_success.html')


def laghu_rudra_yajman_form_view(request):
    if request.method == 'POST':
        registered_by = (request.POST.get('registered_by') or '').strip()
        registered_mobile = (request.POST.get('registered_mobile') or '').strip()
        husband_name = (request.POST.get('husband_name') or '').strip()
        wife_name = (request.POST.get('wife_name') or '').strip()
        city = (request.POST.get('city') or '').strip()
        contact_number = (request.POST.get('contact_number') or '').strip()
        full_address = (request.POST.get('full_address') or '').strip()

        try:
            if not registered_by:
                raise ValueError('Please enter the form registrant name.')
            if not re.fullmatch(r'\d{10}', registered_mobile):
                raise ValueError('Please enter a valid 10-digit mobile number for the registrant.')
            if not husband_name:
                raise ValueError('Please enter the husband name.')
            if not wife_name:
                raise ValueError('Please enter the wife name.')
            if not city:
                raise ValueError('Please enter the city.')
            if not re.fullmatch(r'\d{10}', contact_number):
                raise ValueError('Please enter a valid 10-digit contact number.')
            if not full_address:
                raise ValueError('Please enter the full address.')

            LaghuRudraYajmanRegistration.objects.create(
                registered_by=registered_by,
                registered_mobile=registered_mobile,
                husband_name=husband_name,
                wife_name=wife_name,
                city=city,
                contact_number=contact_number,
                full_address=full_address,
            )
            return redirect('laghu_rudra_yajman_success')
        except ValueError as exc:
            return render(
                request,
                'biodata/Laghu_rudra_yajman_Form.html',
                {'error': str(exc), 'form_data': request.POST}
            )
        except Exception:
            return render(
                request,
                'biodata/Laghu_rudra_yajman_Form.html',
                {'error': 'Something went wrong while saving your form. Please try again.', 'form_data': request.POST}
            )

    return render(request, 'biodata/Laghu_rudra_yajman_Form.html')


def laghu_rudra_yajman_success(request):
    return render(request, 'biodata/laghu_rudra_yajman_success.html')


def shiv_manadir_shivalay_info_view(request):
    if request.method == 'POST':
        temple_name = (request.POST.get('temple_name') or '').strip()
        priest_president_name = (request.POST.get('priest_president_name') or '').strip()
        priest_president_phone = (request.POST.get('priest_president_phone') or '').strip()
        city = (request.POST.get('city') or '').strip()
        form_filled_by = (request.POST.get('form_filled_by') or '').strip()
        form_filler_phone = (request.POST.get('form_filler_phone') or '').strip()

        try:
            if not temple_name:
                raise ValueError('Please enter the Shiv Mandir / Shivālay name.')
            if not priest_president_name:
                raise ValueError('Please enter the priest or president name.')
            if not re.fullmatch(r'\d{10}', priest_president_phone):
                raise ValueError('Please enter a valid 10-digit priest / president phone number.')
            if not city:
                raise ValueError('Please enter the city.')
            if not form_filled_by:
                raise ValueError('Please enter the name of the person filling the form.')
            if not re.fullmatch(r'\d{10}', form_filler_phone):
                raise ValueError('Please enter a valid 10-digit form filler phone number.')

            ShivMandirShivalayInfo.objects.create(
                temple_name=temple_name,
                priest_president_name=priest_president_name,
                priest_president_phone=priest_president_phone,
                city=city,
                form_filled_by=form_filled_by,
                form_filler_phone=form_filler_phone,
            )
            return redirect('shiv_manadir_shivalay_info_success')
        except ValueError as exc:
            return render(
                request,
                'biodata/shiva_manadir_shivalay_info.html',
                {'error': str(exc), 'form_data': request.POST}
            )
        except Exception:
            return render(
                request,
                'biodata/shiva_manadir_shivalay_info.html',
                {'error': 'Something went wrong while saving your form. Please try again.', 'form_data': request.POST}
            )

    return render(request, 'biodata/shiva_manadir_shivalay_info.html')


def shiv_manadir_shivalay_info_success(request):
    return render(request, 'biodata/shiva_manadir_shivalay_info_success.html')
