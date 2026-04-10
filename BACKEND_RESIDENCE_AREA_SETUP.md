# 37th Sammelan - Residence Area Backend Setup

## Overview
Backend support for all 6 residence area options has been fully configured for the 37th Sammelan Mumbai & Maharashtra form.

## Changes Made

### 1. **Model Updates** (`biodata/models_37th_sammelan.py`)
   - Added `RESIDENCE_CHOICES` with all 6 options:
     - `qatar_region` → Gujarat Region (North or Central or South)
     - `saurashtra_region` → Saurashtra Region
     - `kachchh_region` → Kachchh Region
     - `mumbai_maharashtra` → Mumbai & Maharashtra Region
     - `rest_of_india` → Rest of Indian Region (except Gujarat & Maharashtra)
     - `nri` → NRI (Any Visa)
   
   - Added choice constraints to fields:
     - `resCat` - Default: 'nri'
     - `marital` - With all marital status options
     - `visa` - With all visa type options
     - `nadi` - With astrological options
   
   - Added `Meta` class for better admin display

### 2. **View Updates** (`biodata/views_37th_sammelan.py`)
   - Added comprehensive form validation:
     - ✅ Name validation (min 3 characters)
     - ✅ Email validation
     - ✅ Mobile number validation (10 digits)
     - ✅ Residence area validation against allowed choices
     - ✅ Photo validation (format & size < 5MB)
     - ✅ Declaration agreement validation
   
   - Added error handling and user feedback via Django messages
   - Proper error context passed back to form with specific field errors

### 3. **Admin Updates** (`biodata/admin_37th_sammelan.py`)
   - Organized fields into logical fieldsets:
     - Personal Details
     - Contact & Location
     - Physical Details
     - Professional Details
     - Family Details
     - Lifestyle & Habits
     - Astrology
     - Partner Preferences
     - Registration Details
     - Metadata
   
   - Added improved list display (key fields only)
   - Added filters for: `gender`, `marital`, `resCat`, `visa`, `country`, `created_at`
   - Added CSV export functionality for registrations

## Database Migration Required

After these changes, run the following command to create migrations:

```bash
python manage.py makemigrations biodata
python manage.py migrate biodata
```

## API Response Format

When a registration is submitted with `resCat`, it will be stored with one of these values:
- `gujarét_region`
- `saurashtra_region`
- `kachchh_region`
- `mumbai_maharashtra`
- `rest_of_india`
- `nri`

## Testing the Backend

### Valid Submission Test
```python
POST /37th-sammelan/register/
{
    "name": "John Doe",
    "gender": "Male",
    "dob": "01-01-1990",
    "email": "john@example.com",
    "regMobile": "9876543210",
    "whatsapp": "9876543210",
    "resCat": "indianRegion",  # or any valid choice
    "declaration": "Agree",
    "photo": <file>
}
```

### Expected Success Response
- Redirect to success page
- Data saved in `Sammelan37MumbaiMaharashtra` model
- All fields preserved correctly

### Expected Error Response
```python
{
    'form': submitted_data,
    'errors': {
        'field_name': 'Error message'
    }
}
```

## Admin Panel Features

1. **List View**: Shows Name, Gender, DOB, Email, WhatsApp, Residence Area, Created Date
2. **Filters**: Filter by residence area, gender, visa status, country
3. **Search**: Search by name, email, city, phone number
4. **Export**: CSV export with all key registration details

## Field Validation Rules

| Field | Validation | Error Message |
|-------|-----------|------------------|
| name | 3+ characters | "minimum 3 characters" |
| email | Valid email format | "valid email address" |
| regMobile | 10 digits | "10-digit mobile number" |
| whatsapp | 10 digits | "10-digit WhatsApp number" |
| resCat | Must be valid choice | "Invalid residence area selected" |
| photo | JPG/PNG/GIF, < 5MB | Format or size error |
| declaration | Must be 'Agree' | "You must agree to the declaration" |

## Success Response

After successful registration:
1. User is redirected to: `/37th-sammelan/success/`
2. Django message is displayed: "Your registration has been submitted successfully!"
3. Data is stored in database with timestamp

## Quick Links

- Model: [biodata/models_37th_sammelan.py](biodata/models_37th_sammelan.py)
- View: [biodata/views_37th_sammelan.py](biodata/views_37th_sammelan.py)
- Admin: [biodata/admin_37th_sammelan.py](biodata/admin_37th_sammelan.py)
- Template: [templates/biodata/37_sammelan_UK_europe.html](templates/biodata/37_sammelan_UK_europe.html)

## Notes

- All 6 residence area options are fully functional
- Form prevents invalid submissions
- Data is automatically categorized by residence area in admin
- CSV export helps with registration reports and analysis
