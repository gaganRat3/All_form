import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','biodata_project.settings')
django.setup()
from django.contrib import admin
from biodata.models import StorySubmission

ma = admin.site._registry.get(StorySubmission)
print('StorySubmission registered:', ma is not None)
if ma:
    print('ModelAdmin class:', type(ma).__name__)
    print('Declared actions:', getattr(ma, 'actions', None))
    # Also list methods with admin action attribute
    actions = []
    for name in dir(ma):
        attr = getattr(ma, name)
        if hasattr(attr, 'short_description') or hasattr(attr, 'description'):
            if callable(attr):
                actions.append(name)
    print('Callable methods with admin descriptions (candidates):', actions)
