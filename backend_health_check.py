#!/usr/bin/env python
"""
Backend Health Check Script
Verifies the Django backend is properly configured and all models/migrations are in sync.
"""

import os
import sys
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biodata_project.settings')
django.setup()

from django.apps import apps
from django.db import connection
from django.core.management import call_command
from io import StringIO

def print_section(title):
    """Print a section header"""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")

def check_installed_apps():
    """Check if biodata app is properly installed"""
    print_section("1. CHECKING INSTALLED APPS")
    
    apps_list = apps.get_app_configs()
    biodata_installed = False
    
    for app in apps_list:
        if app.name == 'biodata':
            biodata_installed = True
            print(f"✅ biodata app is installed")
            print(f"   Location: {app.module_dir}")
            break
    
    if not biodata_installed:
        print("❌ ERROR: biodata app is NOT installed in INSTALLED_APPS")
        return False
    
    return True

def check_models():
    """Check if all models are properly defined"""
    print_section("2. CHECKING MODELS")
    
    from biodata.models import SaurasthraKutchSammelan, FortyPlusSammelan
    
    models_check = {
        'SaurasthraKutchSammelan': SaurasthraKutchSammelan,
        'FortyPlusSammelan': FortyPlusSammelan,
    }
    
    for model_name, model_class in models_check.items():
        print(f"✅ {model_name} model is defined")
        print(f"   Fields: {len(model_class._meta.fields)}")
    
    return True

def check_admin_registration():
    """Check if models are registered in admin"""
    print_section("3. CHECKING ADMIN REGISTRATION")
    
    from django.contrib import admin
    from biodata.models import SaurasthraKutchSammelan, FortyPlusSammelan
    
    admin_models = [model for model, _ in admin.site._registry.items()]
    
    models_to_check = [SaurasthraKutchSammelan, FortyPlusSammelan]
    
    for model in models_to_check:
        if model in admin_models:
            print(f"✅ {model.__name__} is registered in Django Admin")
        else:
            print(f"❌ {model.__name__} is NOT registered in Django Admin")
    
    return True

def check_migrations():
    """Check migration status"""
    print_section("4. CHECKING MIGRATIONS")
    
    # Get list of migration files
    migrations_dir = Path('biodata/migrations')
    if migrations_dir.exists():
        migration_files = sorted([f.name for f in migrations_dir.glob('*.py') if f.name != '__init__.py'])
        print(f"✅ Total migrations found: {len(migration_files)}")
        print(f"   Latest migration: {migration_files[-1] if migration_files else 'None'}")
        
        # Check for SaurasthraKutchSammelan migration
        saurashtra_migration = any('saurasthrakutchsammelan' in f.lower() for f in migration_files)
        if saurashtra_migration:
            print(f"✅ SaurasthraKutchSammelan migration exists")
        else:
            print(f"⚠️  SaurasthraKutchSammelan migration may be missing or has a different name")
    else:
        print("❌ migrations directory not found")
        return False
    
    return True

def check_database_tables():
    """Check if database tables exist"""
    print_section("5. CHECKING DATABASE TABLES")
    
    cursor = connection.cursor()
    
    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    
    print(f"Total tables in database: {len(tables)}\n")
    
    critical_tables = [
        'biodata_saurasthrakutchsammelan',
        'biodata_fortyplussammelan',
        'biodata_candidatebiodata',
    ]
    
    for table in critical_tables:
        if table in tables:
            print(f"✅ Table '{table}' exists")
        else:
            print(f"❌ Table '{table}' is MISSING - Run migrations!")
    
    return all(table in tables for table in critical_tables)

def check_migrations_state():
    """Check if there are unapplied migrations"""
    print_section("6. CHECKING MIGRATION STATE")
    
    # Capture makemigrations output
    out = StringIO()
    try:
        call_command('makemigrations', '--dry-run', stdout=out, stderr=out)
        output = out.getvalue()
        
        if 'No changes detected' in output:
            print("✅ All models are in sync with migrations")
            return True
        else:
            print("⚠️  Potential unapplied changes detected:")
            print(output)
            return False
    except Exception as e:
        print(f"⚠️  Could not check migration state: {e}")
        return False

def check_forms():
    """Check if forms are properly defined"""
    print_section("7. CHECKING FORMS")
    
    try:
        from biodata.forms import SaurasthraKutchSammelanForm, FortyPlusSammelanForm
        print(f"✅ SaurasthraKutchSammelanForm is defined")
        print(f"✅ FortyPlusSammelanForm is defined")
        return True
    except ImportError as e:
        print(f"❌ Error importing forms: {e}")
        return False

def check_urls():
    """Check if URLs are configured"""
    print_section("8. CHECKING URL CONFIGURATION")
    
    try:
        # Try to import urls
        from biodata import urls
        print(f"✅ biodata/urls.py can be imported")
        return True
    except Exception as e:
        print(f"❌ Error with URL configuration: {e}")
        return False

def generate_recommendations(failed_checks):
    """Generate recommendations based on failed checks"""
    print_section("RECOMMENDATIONS")
    
    if not failed_checks:
        print("✅ All checks passed! Your backend appears to be properly configured.")
        return
    
    print("To fix the issues, run these commands in order:\n")
    
    recommendations = [
        "python manage.py makemigrations biodata",
        "python manage.py migrate biodata",
        "python manage.py check",
    ]
    
    for i, cmd in enumerate(recommendations, 1):
        print(f"{i}. python manage.py {cmd.split('manage.py ')[1]}")
    
    print("\nOr run the apply_migrations.py helper script:")
    print("  python apply_migrations.py")

def main():
    """Run all checks"""
    print("\n" + "="*70)
    print(" " * 15 + "DJANGO BACKEND HEALTH CHECK")
    print("="*70)
    
    checks = [
        ("Installed Apps", check_installed_apps),
        ("Models", check_models),
        ("Admin Registration", check_admin_registration),
        ("Migrations", check_migrations),
        ("Database Tables", check_database_tables),
        ("Migration State", check_migrations_state),
        ("Forms", check_forms),
        ("URLs", check_urls),
    ]
    
    failed_checks = []
    
    for check_name, check_func in checks:
        try:
            if not check_func():
                failed_checks.append(check_name)
        except Exception as e:
            print(f"❌ Error during {check_name} check: {e}")
            failed_checks.append(check_name)
    
    # Generate recommendations
    generate_recommendations(failed_checks)
    
    print("\n" + "="*70)
    if failed_checks:
        print(f"❌ FAILED: {len(failed_checks)} check(s) failed")
        print("="*70 + "\n")
        return 1
    else:
        print("✅ SUCCESS: All checks passed!")
        print("="*70 + "\n")
        return 0

if __name__ == '__main__':
    sys.exit(main())
