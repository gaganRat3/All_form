#!/usr/bin/env python
"""
Helper script to apply the missing SaurasthraKutchSammelan migration.
Run this from the project root directory.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biodata_project.settings')
django.setup()

from django.core.management import call_command

print("=" * 60)
print("Applying pending migrations...")
print("=" * 60)

try:
    # Apply all pending migrations
    call_command('migrate', 'biodata')
    print("\n✅ SUCCESS: Migrations applied successfully!")
    print("\nYou can now access the Django admin:")
    print("  - URL: http://127.0.0.1:8000/admin/biodata/saurasthrakutchsammelan/")
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    sys.exit(1)
