@echo off
REM Run this in your VS Code terminal to fix the error

echo.
echo ======================================================================
echo      FIXING: no such table: biodata_saurasthrakutchsammelan
echo ======================================================================
echo.

echo Step 1: Applying Django migrations...
echo.
python manage.py migrate biodata

echo.
echo Step 2: Verifying the fix...
echo.
python manage.py shell -c "from django.db import connection; cursor = connection.cursor(); cursor.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name='biodata_saurasthrakutchsammelan';\"); print('✅ SUCCESS! Table exists!' if cursor.fetchone() else '❌ ERROR: Table still missing')"

echo.
echo ======================================================================
echo      FIXED! Access: http://127.0.0.1:8000/admin/biodata/saurasthrakutchsammelan/
echo ======================================================================
echo.

pause
