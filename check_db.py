import os
import django
import sqlite3

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biodata_project.settings')
django.setup()

from django.conf import settings
from biodata.models import CourierBooklet35thBooking

# Get database path
db_path = settings.DATABASES['default']['NAME']
print(f"Database path: {db_path}")
print(f"Database exists: {os.path.exists(db_path)}")

# Connect to database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check if table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='biodata_courierbooklet35thbooking';")
table_exists = cursor.fetchone()
print(f"Table exists: {table_exists}")

if table_exists:
    # Count rows
    cursor.execute("SELECT COUNT(*) FROM biodata_courierbooklet35thbooking;")
    count = cursor.fetchone()[0]
    print(f"Row count in biodata_courierbooklet35thbooking: {count}")
    
    # Get all rows
    cursor.execute("SELECT id, name, city, email FROM biodata_courierbooklet35thbooking;")
    rows = cursor.fetchall()
    print(f"Rows: {rows}")

# Check Django ORM
print(f"\nDjango ORM count: {CourierBooklet35thBooking.objects.count()}")
print(f"Django ORM all: {list(CourierBooklet35thBooking.objects.all())}")

conn.close()
