#!/usr/bin/env python
"""
Debug script to check form submission and database status
Run this to see where the data is going
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biodata_project.settings')
django.setup()

from django.db import connection
from biodata.models import SaurasthraKutchSammelan
from django.apps import apps

print("\n" + "="*70)
print("  SAURASHTRA & KUTCH SAMMELAN - DEBUG CHECK")
print("="*70 + "\n")

# Check 1: Database table exists
print("1️⃣  CHECKING DATABASE TABLE...")
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='biodata_saurasthrakutchsammelan';")
table_exists = cursor.fetchone()

if table_exists:
    print("   ✅ Table exists: biodata_saurasthrakutchsammelan")
else:
    print("   ❌ Table does NOT exist!")
    print("   Run this to create it: python manage.py migrate")

# Check 2: Total records in database
print("\n2️⃣  CHECKING DATA IN DATABASE...")
try:
    count = SaurasthraKutchSammelan.objects.count()
    print(f"   ✅ Total records: {count}")
    
    if count > 0:
        print("\n   📋 List of all records:")
        for i, record in enumerate(SaurasthraKutchSammelan.objects.all(), 1):
            print(f"      {i}. {record.name} | {record.email} | ID: {record.id}")
    else:
        print("   ⚠️  No records found. Check if form is submitting correctly.")
except Exception as e:
    print(f"   ❌ Error: {e}")
    print("   The table might not exist. Run: python manage.py migrate")

# Check 3: Model fields
print("\n3️⃣  CHECKING MODEL FIELDS...")
model = apps.get_model('biodata', 'SaurasthraKutchSammelan')
fields = [f.name for f in model._meta.get_fields()]
print(f"   ✅ Total fields in model: {len(fields)}")
print(f"   Fields: {', '.join(fields[:10])}...")

# Check 4: Form validation test
print("\n4️⃣  CHECKING FORM FIELDS...")
from biodata.forms import SaurasthraKutchSammelanForm
form = SaurasthraKutchSammelanForm()
form_fields = list(form.fields.keys())
print(f"   ✅ Form has {len(form_fields)} fields:")
for field in form_fields:
    print(f"      - {field}")

print("\n" + "="*70)
print("  NEXT STEPS:")
print("="*70)
print("\nIf you see 'Table does NOT exist':")
print("  1. Run: python manage.py migrate")
print("  2. Then refresh the admin page\n")

print("If table exists but no data:")
print("  1. Check browser console for JavaScript errors")
print("  2. Try submitting the form again")
print("  3. Check Django logs for POST errors\n")

print("="*70 + "\n")
