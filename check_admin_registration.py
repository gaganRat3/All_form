import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biodata_project.settings')
django.setup()

from django.contrib import admin
from biodata.models import StorySubmission

registered = StorySubmission in admin.site._registry
print('StorySubmission registered in admin:', registered)
if registered:
    print('Registered ModelAdmin:', type(admin.site._registry[StorySubmission]).__name__)
    print('ModelAdmin repr:', repr(admin.site._registry[StorySubmission]))
else:
    print('StorySubmission not found in admin registry')
