#!/bin/bash
# Run this in your VS Code terminal to fix the SaurasthraKutchSammelan table error

echo "======================================================================"
echo "     FIXING: no such table: biodata_saurasthrakutchsammelan"
echo "======================================================================"

cd "$(dirname "$0")" || exit

echo ""
echo "Step 1: Applying Django migrations..."
echo "------"
python manage.py migrate biodata

echo ""
echo "Step 2: Verifying the fix..."
echo "------"
python manage.py shell << EOF
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='biodata_saurasthrakutchsammelan';")
table_exists = cursor.fetchone()
if table_exists:
    print("✅ SUCCESS! Table 'biodata_saurasthrakutchsammelan' now exists!")
else:
    print("❌ ERROR: Table still doesn't exist")
EOF

echo ""
echo "======================================================================"
echo "     FIXED! You can now access: /admin/biodata/saurasthrakutchsammelan/"
echo "======================================================================"
