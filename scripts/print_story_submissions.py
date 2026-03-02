import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biodata_project.settings')
django.setup()

from biodata.models import StorySubmission

qs = StorySubmission.objects.all().order_by('-submitted_at')
print('StorySubmission count:', qs.count())
rows = []
for o in qs[:50]:
    rows.append({
        'id': o.id,
        'boy_name': o.boy_name,
        'girl_name': o.girl_name,
        'function_date': str(o.function_date) if o.function_date else None,
        'message': (o.message[:200] + '...') if o.message and len(o.message) > 200 else o.message,
        'image_path': getattr(o.image, 'path', None),
        'image_url': getattr(o.image, 'url', None),
        'submitted_at': str(o.submitted_at) if o.submitted_at else None,
    })
print(json.dumps(rows, indent=2, ensure_ascii=False))
