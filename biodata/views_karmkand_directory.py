import sys
import logging
from django.shortcuts import render, redirect
from .forms_karmkand_directory import GlobalKarmkandDirectoryForm
from .models_karmkand_directory import GlobalKarmkandDirectoryEntry

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
