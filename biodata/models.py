# Ensure models is imported for new model
from django.db import models
# 40 Plus Sammelan Form Model
class FortyPlusSammelan(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    marital = models.CharField(max_length=50)
    disability = models.TextField(blank=True)
    tob = models.CharField(max_length=20, blank=True)
    birthPlace = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    visa = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=10, blank=True)
    weight = models.CharField(max_length=10, blank=True)
    education = models.CharField(max_length=100, blank=True)
    educationDetail = models.CharField(max_length=200, blank=True)
    occupationCat = models.CharField(max_length=100, blank=True)
    occupationDetails = models.TextField(blank=True)
    salary = models.CharField(max_length=20, blank=True)
    shani = models.CharField(max_length=30, blank=True)
    hobbies = models.CharField(max_length=200, blank=True)
    father = models.CharField(max_length=100, blank=True)
    mother = models.CharField(max_length=100, blank=True)
    fatherWp = models.CharField(max_length=20, blank=True)
    motherWp = models.CharField(max_length=20, blank=True)
    caste = models.CharField(max_length=100, blank=True)
    gotra = models.CharField(max_length=100, blank=True)
    kuldevi = models.CharField(max_length=100, blank=True)
    siblings = models.TextField(blank=True)
    eating_habbits = models.CharField(max_length=100, blank=True)
    alcohol = models.CharField(max_length=10, blank=True)
    smoke = models.CharField(max_length=10, blank=True)
    other_habbit = models.CharField(max_length=100, blank=True)
    legal_case = models.CharField(max_length=100, blank=True)
    locChoice = models.CharField(max_length=100, blank=True)
    ageGap = models.CharField(max_length=20, blank=True)
    eduChoice = models.CharField(max_length=100, blank=True)
    otherChoice = models.TextField(blank=True)
    who = models.CharField(max_length=100, blank=True)
    regMobile = models.CharField(max_length=20)
    resCat = models.CharField(max_length=50, blank=True)
    nadi = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='40plus_sammelan_photos/', blank=True)
    declaration = models.CharField(max_length=10)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "40 Plus Sammelan Registration"
        verbose_name_plural = "40 Plus Sammelan Registrations"

from django.db import models
from .models_booklet_camp_adv import BookletCampAdvBooking
from django.utils import timezone
from django.db import models

# Model for Booklet Library form submissions
class BookletLibrarySubmission(models.Model):
    name = models.CharField(max_length=255)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    email = models.EmailField()
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.city} - {self.email}"
import uuid
from django.db import models




class BncBnfApplication(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    MARRIAGE_STATUS_CHOICES = [
        ('Married', 'Married'),
        ('Unmarried', 'Unmarried'),
        ('Divorce', 'Divorce'),
        ('Widow', 'Widow'),
    ]

    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    date_of_birth = models.CharField(max_length=20)
    marriage_status = models.CharField(max_length=10, choices=MARRIAGE_STATUS_CHOICES)
    whatsapp_number = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    current_city = models.CharField(max_length=100)
    area_name = models.CharField(max_length=100, blank=True)
    home_address = models.TextField()

    def __str__(self):
        return self.full_name
# Removed duplicate MegaBookletCorrectionRequest model as per user request

# Model for 35th Courier Booklet
class CourierBooklet35thBooking(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=20)
    email = models.EmailField()
    girls_booklet_with = models.BooleanField(default=False)
    boys_booklet_with = models.BooleanField(default=False)
    courier_address = models.TextField(blank=True, null=True)
    payment_screenshot = models.ImageField(upload_to='payment_screenshots/')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "35th Courier Booklet Booking"
        verbose_name_plural = "35th Courier Booklet Bookings"
        ordering = ['-created_at']

    def __str__(self):
        courier_info = "With Courier" if self.courier_address else "No Courier"
        return f"{self.name} - {courier_info}"

class GarbaPassRegistration(models.Model):
    PASS_TYPE_CHOICES = [
        ('Garba Pass', 'Garba Pass'),
        ('Garba Pass For Others', 'Garba Pass For Others'),
        ('Dinner Pass', 'Dinner Pass'),
    ]
    full_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=20, null=True, blank=True)
    residence_city = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=15)
    passes = models.JSONField()  # Example: [{"type": "Garba Pass", "quantity": 2, "amount": 100}]
    subtotal = models.PositiveIntegerField()
    payment_screenshot = models.ImageField(upload_to='payment_screenshots/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.whatsapp_number}"

class AudienceRegistration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)
    ticket_quantity = models.PositiveIntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=50.00)
    payment_screenshot = models.ImageField(upload_to='audience_payment_screenshots/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone_number}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class CandidateBiodata(models.Model):
    # Personal Details
    candidate_name = models.CharField(max_length=255)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    registration_by = models.CharField(max_length=255, blank=True, null=True)
    registrant_mobile = models.CharField(max_length=20, unique=True)
    candidate_current_city = models.CharField(max_length=255, blank=False, null=False)
    dob = models.CharField(max_length=50, blank=True, null=True)
    MARITAL_STATUS_CHOICES = [
        ('never_married', 'Never Married (Unmarried)'),
        ('divorce_no_child', 'Divorce (No Child)'),
        ('divorce_having_child', 'Divorce (Having Child)'),
        ('widow_no_child', 'Widow (No Child)'),
        ('widow_having_child', 'Widow (Having Child)'),
        ('divorce_annulled', 'Divorce (Annulled)'),
        ('divorce_in_process', 'Divorce in Process'),
        ('separated', 'Separated'),
        ('gol_dhana_cancel', '1 Time Gol-Dhana Done, but then Cancelled'),
        ('engagement_cancel', '1 Time Engagement Done, but then Cancelled'),
    ]
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES, default='never_married')
    DISABILITY_CHOICES = [
        ('No', 'No'),
        ('Yes', 'Yes'),
        ('Minor Problem', 'Minor Problem'),
    ]
    birth_time = models.CharField(max_length=50, blank=True, null=True)
    birth_place = models.CharField(max_length=255)
    RESIDENCE_AREA_CATEGORY_CHOICES = [
        ('gujarat', 'Gujarat Region (North or Central or South)'),
        ('saurashtra', 'Saurashtra Region'),
        ('kachchh', 'Kachchh Region'),
        ('mumbai_maharashtra', 'Mumbai & Maharashtra Region'),
        ('rest_of_india', 'Root of Indian Region (except Gujarat & Maharashtra)'),
        ('nri', 'NRI (Any Visa)'),
    ]
    residence_area_category = models.CharField(max_length=100, choices=RESIDENCE_AREA_CATEGORY_CHOICES, blank=True, null=True)
    current_country = models.CharField(max_length=255, blank=True, null=True)
    VISA_STATUS_CHOICES = [
        ('Indian Citizen', 'Indian Citizen'),
        ('NRI - Student Visa', 'NRI - Student Visa'),
        ('NRI - Work Permit', 'NRI - Work Permit'),
        ('NRI - PR', 'NRI - PR'),
        ('NRI - PR In Process', 'NRI - PR In Process'),
        ('NRI - Green Card (USA)', 'NRI - Green Card (USA)'),
        ('NRI - Blue Card (EU)', 'NRI - Blue Card (EU)'),
        ('NRI - Citizenship', 'NRI - Citizenship'),
        ('NRI - Visitor Visa', 'NRI - Visitor Visa'),
        ('NRI - H1B (USA)', 'NRI - H1B (USA)'),
        ('NRI - Business Visa', 'NRI - Business Visa'),
        ('NRI - OCI', 'NRI - OCI'),
        ('NRI - F1', 'NRI - F1'),
    ]
    visa_status = models.CharField(max_length=30, choices=VISA_STATUS_CHOICES, default='Indian Citizen')
    visa_status_details = models.CharField(max_length=255, blank=True, null=True, editable=False)
    height = models.CharField(max_length=50, blank=True, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    EDUCATION_CHOICES = [
        ('Undergraduate', 'Undergraduate (10th 12th Pass / Fail , Diploma , ITI , Not Completed Graduation)'),
        ('Graduate', 'Graduate (BA , B.Com. , B.Sc. , BE , BTech, LLB , B. Arch., BBA , BCA etc)'),
        ('Masters', 'Masters (MA , MCom., MSc., ME , MTech, M.Arch , M.Phil, etc Masters Degree holders)'),
        ('CA_CS_ICWA_CPA_ACCA_CIMA', 'CA , CS , ICWA , CPA , ACCA , CIMA , etc'),
        ('Doctor', 'Doctor - Medical - Pharmacy - Dentist - Physiotherapist - Paramedical - Nursing'),
        ('PhD_UPSC_GPSC', 'PhD , UPSC , GPSC (IAS , IPS, etc) , Mayor , Civil Services etc'),
        ('Other', 'Any Other Education Category'),
    ]
    education = models.CharField(max_length=255, choices=EDUCATION_CHOICES)
    OCCUPATION_CHOICES = [
        ('Government Job', 'Government Job'),
        ('Private MNC Job', 'Private MNC Job'),
        ('Self Employed (Own Practice)', 'Self Employed (Own Practice)'),
        ('Own Business', 'Own Business'),
        ('Job + Business', 'Job + Business'),
        ('Free Lancing', 'Free Lancing'),
        ('Student (Studies Running)', 'Student (Studies Running)'),
        ('Searching Job', 'Searching Job'),
        ('Home Works (ghar-kaam)', 'Home Works (ghar-kaam)'),
    ]
    occupation = models.CharField(max_length=255, choices=OCCUPATION_CHOICES)
    occupation_details = models.TextField(blank=True, null=True)
    monthly_income = models.CharField(max_length=100, blank=True, null=True)
    SHANI_MANGAL_CHOICES = [
        ('Yes ( Nirdosh )', 'Yes ( Nirdosh )'),
        ('Yes ( Normal)', 'Yes ( Normal)'),
        ('No', 'No'),
        ("Don't Know", "Don't Know"),
        ("Dont't Believe", "Dont't Believe"),
    ]
    shani_mangal = models.CharField(max_length=20, choices=SHANI_MANGAL_CHOICES, blank=True, null=True)

    NADI_CHOICES = [
        ('Aadhya', 'Aadhya'),
        ('Madhya', 'Madhya'),
        ('Antya', 'Antya'),
        ("I Dont Know", "I Dont Know"),
        ("We Dont Believe", "We Dont Believe"),
    ]
    nadi = models.CharField(max_length=20, choices=NADI_CHOICES, blank=True, null=True)

    # Contact Details
    email = models.EmailField(max_length=254, blank=False, null=False)
    whatsapp_number = models.CharField(max_length=20, blank=False, null=False)

    # Family Details
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    father_mobile = models.CharField(max_length=20)
    mother_mobile = models.CharField(max_length=20)
    type_of_brahmin = models.CharField(max_length=255, blank=True, null=True)
    gotra = models.CharField(max_length=255, blank=True, null=True)
    kuldevi = models.CharField(max_length=255, blank=True, null=True)
    siblings = models.CharField(max_length=255, blank=True, null=True)

    # Partner Preferences
    partner_location = models.CharField(max_length=255, blank=True, null=True)
    partner_age_bracket = models.CharField(max_length=100, blank=True, null=True)
    partner_education = models.CharField(max_length=255, blank=True, null=True)
    other_specific_choice = models.TextField(blank=True, null=True)

    # Photograph - use standard ImageField for local storage
    photograph = models.ImageField(upload_to='photographs/')

    submitted_at = models.DateTimeField(auto_now_add=True)

    DECLARATION_CHOICES = [
        ('Agree', 'Agree (ઉપર મુજબ હું માનું છું અને તેમ કરીશ) - મારો બાયોડેટા બુકલેટ માં ચોક્કસ સમાવેશ કરશોજી'),
        ('Disagree', 'Disagree (ઉપર મુજબ હું નહિ માનું)  - મારો બાયોડેટા કેન્સલ કરી દેજો'),
    ]
    declaration = models.CharField(max_length=20, choices=DECLARATION_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.candidate_name

        eduChoice = models.CharField(max_length=100)
        otherChoice = models.TextField()
        who = models.CharField(max_length=100)
        regMobile = models.CharField(max_length=20)
        resCat = models.CharField(max_length=50)
        nadi = models.CharField(max_length=50)
        email = models.EmailField()
        whatsapp = models.CharField(max_length=20)
        photo = models.ImageField(upload_to='divorce_sammelan_photos/')
        declaration = models.CharField(max_length=10)
        submitted_at = models.DateTimeField(auto_now_add=True)
class GalleryImage(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='gallery_images/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"

class AdvancePassBooking(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=20)
    email = models.EmailField()
    entry_token_quantity = models.PositiveIntegerField(default=0)
    unlimited_buffet_quantity = models.PositiveIntegerField(default=0)
    payment_screenshot = models.ImageField(upload_to='payment_screenshots/')
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total_amount = (
            (self.entry_token_quantity or 0) * 50 +
            (self.unlimited_buffet_quantity or 0) * 200
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - Entry Token: {self.entry_token_quantity}, Buffet: {self.unlimited_buffet_quantity}"



class StageRegistration(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    name_of_candidate = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    dob = models.CharField(max_length=50)
    current_city = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=20, default="NA")

    def __str__(self):
        return self.name_of_candidate

class AdvanceBookletBooking(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=20)
    email = models.EmailField()
    girls_booklet_with = models.BooleanField(default=False)
    boys_booklet_with = models.BooleanField(default=False)
    courier_address = models.TextField(blank=True, null=True)
    payment_screenshot = models.ImageField(upload_to='payment_screenshots/')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Fix: 'with_courier' attribute does not exist, use 'courier_address' or other appropriate field
        courier_info = "With Courier" if self.courier_address else "No Courier"
        return f"{self.name} - {courier_info}"

class SpotAdvanceBookletBooking(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=20)
    email = models.EmailField()
    saurashtra_booklet = models.BooleanField(default=False)
    gujarat_girls_booklet = models.BooleanField(default=False)
    gujarat_boys_booklet = models.BooleanField(default=False)
    nri_booklet = models.BooleanField(default=False)
    mumbai_booklet = models.BooleanField(default=False)
    divorce_widow_booklet = models.BooleanField(default=False)
    payment_screenshot = models.ImageField(upload_to='payment_screenshots/')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    booklet_camp_city = models.CharField(max_length=100, blank=True, null=True)
    candidate_name_dob = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        # Always show "No Courier" for SpotAdvanceBookletBooking
        courier_info = "No Courier"
        return f"{self.name} - {courier_info}"
    


class ZoomRegistration(models.Model):
    name = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    screenshot = models.ImageField(upload_to='screenshots/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.whatsapp}"

class MegaBookletCorrectionRequest(models.Model):
    request_id = models.CharField(max_length=20, unique=True, editable=False)
    candidate_name = models.CharField(max_length=255)
    dob = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=20)
    booklet_serial = models.CharField(max_length=100)
    booklet_name = models.CharField(max_length=255)
    correction_description = models.TextField()
    photo_upload = models.ImageField(upload_to='mega_correction_photos/', blank=True, null=True)
    submission_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.request_id:
            self.request_id = 'CR' + str(uuid.uuid4().int)[:16]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.candidate_name} - {self.request_id}"


class BirthdayFormSubmission(models.Model):
    candidate_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    mobile_1 = models.CharField(max_length=15)
    mobile_2 = models.CharField(max_length=15, blank=True, null=True)
    mobile_3 = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate_name} - {self.mobile_1}"


class StorySubmission(models.Model):
    """Stores story submissions from the frontend form.

    Reduced to only the fields requested by the client:
    - boy_name, girl_name, girl_birth_date, boy_city, girl_city,
      who_is_filling, mobile_number, relationship_status, function_date,
      message (optional), image
    """
    # Couple info
    boy_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Boy Name')
    girl_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Girl Name')
    # Added boy_birth_date to store boy candidate's birth date as requested
    boy_birth_date = models.DateField(blank=True, null=True, verbose_name='Boy Birth Date')
    girl_birth_date = models.DateField(blank=True, null=True, verbose_name='Girl Birth Date')
    boy_city = models.CharField(max_length=255, blank=True, null=True, verbose_name='Boy City')
    girl_city = models.CharField(max_length=255, blank=True, null=True, verbose_name='Girl City')

    # Contact / meta
    who_is_filling = models.CharField(max_length=255, blank=True, null=True, verbose_name='Who is Filling the Form')
    mobile_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='Mobile Number')
    whatsapp_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='WhatsApp Number')
    relationship_status = models.CharField(max_length=100, blank=True, null=True, verbose_name='Candidate Relationship Status')
    function_date = models.DateField(blank=True, null=True, verbose_name='Function Date')
    message = models.TextField(blank=True, null=True, verbose_name='Message (Optional)')

    # Primary uploaded photo (frontend may send multiple; we keep one as primary)
    image = models.ImageField(upload_to='story_images/', blank=True, null=True, verbose_name='Photos')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Prefer a readable representation using couple names when available
        names = []
        if self.boy_name:
            names.append(self.boy_name)
        if self.girl_name:
            names.append(self.girl_name)
        if names:
            return " & ".join(names)
        return f"StorySubmission {self.pk}"

    class Meta:
        verbose_name = 'Share Your Wedding Story'
        verbose_name_plural = 'Share Your Wedding Stories'


class ParticipantRegistration(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    
    # Event Selections
    events = models.JSONField(default=list)  # Store selected events as JSON array
    
    # Payment Information
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    payment_screenshot = models.ImageField(upload_to='payment_screenshots/')
    
    # Metadata
    submission_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def events_display(self):
        """Return events as comma-separated string for display"""
        if isinstance(self.events, list):
            return ", ".join(self.events)
        return str(self.events)
        # ...existing code...

class BhudevSammelanRegistration(models.Model):
    declaration = models.CharField(max_length=10, choices=[
        ('agree', 'Agree (ઉપર મુજબ હું માનું છું)'),
        ('disagree', 'Disagree (ઉપર મુજબ હું નહિ માનું)'),
    ], blank=True, null=True, default='')
    sr_number = models.AutoField(primary_key=True)
    candidate_name = models.CharField(max_length=200)
    candidate_gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    registrant_relation = models.CharField(max_length=100)
    registrant_mobile = models.CharField(max_length=20)
    candidate_current_city = models.CharField(max_length=100)
    dob = models.CharField(max_length=30)
    marital_status = models.CharField(max_length=50, choices=[
        ('never_married', 'Never Married (Unmarried)'),
        ('divorce_no_child', 'Divorce (No Child)'),
        ('divorce_having_child', 'Divorce (Having Child)'),
        ('widow_no_child', 'Widow (No Child)'),
        ('widow_having_child', 'Widow (Having Child)'),
        ('divorce_annulled', 'Divorce (Annulled)'),
        ('divorce_in_process', 'Divorce in Process'),
        ('separated', 'Separated'),
        ('gol_dhana_cancel', '1 Time Gol-Dhana Done, but then Cancelled'),
        ('engagement_cancel', '1 Time Engagement Done, but then Cancelled'),
    ])
    birth_time = models.CharField(max_length=30, blank=True)
    birth_place = models.CharField(max_length=100, blank=True)
    hobbies = models.CharField(max_length=255, blank=True, null=True, verbose_name='Hobbies')
    residence_area_category = models.CharField(max_length=50, choices=[
        ('gujarat', 'Gujarat Region (North or Central or South)'),
        ('saurashtra', 'Saurashtra Region'),
        ('kachchh', 'Kachchh Region'),
        ('mumbai_maharashtra', 'Mumbai & Maharashtra Region'),
        ('rest_of_india', 'Rest of Indian Region (except Gujarat & Maharashtra)'),
        ('nri', 'NRI (Any Visa)'),
    ], blank=True, null=True, verbose_name='Residence Area Category')
    current_country = models.CharField(max_length=50)
    visa_status = models.CharField(max_length=30, choices=[
        ('indian_citizen', 'Indian Citizen'),
        ('nri_student_visa', 'NRI - Student Visa'),
        ('nri_work_permit', 'NRI - Work Permit'),
        ('nri_pr', 'NRI - PR'),
        ('nri_pr_in_process', 'NRI - PR In Process'),
        ('nri_green_card_usa', 'NRI - Green Card (USA)'),
        ('nri_blue_card_eu', 'NRI - Blue Card (EU)'),
        ('nri_citizenship', 'NRI - Citizenship'),
        ('nri_visitor_visa', 'NRI - Visitor Visa'),
        ('nri_h1b_usa', 'NRI - H1B (USA)'),
        ('nri_business_visa', 'NRI - Business Visa'),
        ('nri_oci', 'NRI - OCI'),
        ('nri_f1', 'NRI - F1'),
    ])
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    education_category = models.CharField(max_length=100, choices=[
        ('undergraduate', 'Undergraduate (10th 12th Pass / Fail , Diploma , ITI , Not Completed Graduation)'),
        ('graduate', 'Graduate (BA , B.Com. , B.Sc. , BE , BTech, LLB , B. Arch., BBA , BCA etc)'),
        ('masters', 'Masters (MA , MCom, MSc., ME , MTech, M.Arch , M.Phil, LLM, etc)'),
        ('ca_cs', 'CA , CS , ICWA, CPA, ACCA , CIMA , etc'),
        ('doctor_medical', 'Doctor - Medical - Pharmacy - Dentist - Physiotherapist - Paramedical - Nursing - Clinical Surgical - Specialists'),
        ('phd_civil', 'PhD , UPSC, GPSC (IAS , IPS, etc) , Mayor , Civil Services etc'),
        ('other', 'Any Other Education Category'),
    ], verbose_name='Education Category')
    education_detail = models.CharField(max_length=200, blank=True)
    occupation_category = models.CharField(max_length=50, choices=[
        ('government_job', 'Government Job'),
        ('private_mnc_job', 'Private MNC Job'),
        ('self_employed', 'Self Employed (Own Practice)'),
        ('own_business', 'Own Business'),
        ('job_business', 'Job + Business'),
        ('free_lancing', 'Free Lancing'),
        ('student', 'Student (Studies Running)'),
        ('searching_job', 'Searching Job'),
        ('home_works', 'Home Works (ghar-kaam)'),
    ])
    occupation_details = models.CharField(max_length=200, blank=True)
    salary = models.CharField(max_length=20, blank=True)
    shani_mangal = models.CharField(max_length=30, choices=[
        ('yes_shani', 'Yes (Shani)'),
        ('yes_mangal', 'Yes (Mangal)'),
        ('no', 'No'),
        ('dont_know', "Don't Know"),
        ('dont_believe', "We Don't Believe"),
    ], verbose_name='Shani / Mangal', blank=True, null=True)
    nadi = models.CharField(max_length=30, choices=[
        ('aadhya', 'Aadhya'),
        ('madhya', 'Madhya'),
        ('antya', 'Antya'),
        ('dont_know', 'I Dont Know'),
        ('dont_believe', "We Don't Believe"),
    ], blank=True, null=True)
    email = models.EmailField()
    whatsapp_number = models.CharField(max_length=20)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=20)
    mother_mobile = models.CharField(max_length=20)
    type_of_brahmin = models.CharField(max_length=100)
    gotra = models.CharField(max_length=100)
    disability = models.TextField(blank=True)

    kuldevi = models.CharField(max_length=255, blank=True, null=True)
    siblings = models.CharField(max_length=200, blank=True)

    # Added fields for habits and legal case
    eating_habbits = models.CharField(max_length=100, blank=True, null=True, verbose_name='Eating Habits (Pure Veg?)')
    alcohol = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No')], blank=True, null=True, verbose_name='Alcoholic Drinks?')
    smoke = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No')], blank=True, null=True, verbose_name='Smoke?')
    other_habbit = models.CharField(max_length=100, blank=True, null=True, verbose_name='Any Other Habit?')
    legal_case = models.CharField(max_length=100, blank=True, null=True, verbose_name='Any Legal or Police Case?')

    partner_location = models.CharField(max_length=100, blank=True)
    partner_age_bracket = models.CharField(max_length=50, blank=True)
    partner_education = models.CharField(max_length=100, blank=True)
    other_specific_choice = models.CharField(max_length=200, blank=True)
    photograph = models.ImageField(upload_to='divorce_sammelan_photos/')
    # Declaration field removed as per request
    submitted_at = models.DateTimeField(auto_now_add=True)

    # Admin-only fields
    confirmation_status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("rejected", "Rejected")
        ],
        default="pending",
        blank=True,
        verbose_name="Confirmation Status (Admin)"
    )
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ("unpaid", "Unpaid"),
            ("paid", "Paid"),
            ("partial", "Partial")
        ],
        default="unpaid",
        blank=True,
        verbose_name="Payment Status (Admin)"
    )

    def __str__(self):
        return f"{self.candidate_name} - {self.candidate_gender} - {self.marital_status}"


class SammelanPaymentForm(models.Model):
    name = models.CharField(max_length=255, verbose_name='Full Name')
    date_of_birth = models.CharField(max_length=10, verbose_name='Date of Birth (DD-MM-YYYY)')
    mobile_number = models.CharField(max_length=15, verbose_name='Mobile Number')
    # candidate_email field removed as per request
    marital_status = models.CharField(max_length=100, verbose_name='Marital Status')
    qr_code_image = models.ImageField(upload_to='payment_qr_codes/', blank=True, null=True, verbose_name='QR Code')
    payment_screenshot = models.ImageField(upload_to='payment_screenshots/', verbose_name='Payment Screenshot')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.mobile_number}"


# Divorce Sammelan Form Model
class DivorceSammelanForm(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    marital = models.CharField(max_length=50, choices=[
        ("never_married", "Never Married (Unmarried)"),
        ("divorce_no_child", "Divorce (No Child)"),
        ("divorce_having_child", "Divorce (Having Child)"),
        ("widow_no_child", "Widow (No Child)"),
        ("widow_having_child", "Widow (Having Child)"),
        ("divorce_annulled", "Divorce (Annulled)"),
        ("divorce_in_process", "Divorce in Process"),
        ("separated", "Separated"),
        ("gol_dhana_cancel", "1 Time Gol-Dhana Done, but then Cancelled"),
        ("engagement_cancel", "1 Time Engagement Done, but then Cancelled"),
    ])
    disability = models.TextField()
    tob = models.CharField(max_length=20)
    birthPlace = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    visa = models.CharField(max_length=50)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    education = models.CharField(max_length=100)
    educationDetail = models.CharField(max_length=200)
    occupationCat = models.CharField(max_length=100)
    occupationDetails = models.TextField()
    salary = models.CharField(max_length=20)
    shani = models.CharField(max_length=30)
    hobbies = models.CharField(max_length=200)
    father = models.CharField(max_length=100)
    mother = models.CharField(max_length=100)
    fatherWp = models.CharField(max_length=20)
    motherWp = models.CharField(max_length=20)
    caste = models.CharField(max_length=100)
    gotra = models.CharField(max_length=100)
    kuldevi = models.CharField(max_length=100)
    siblings = models.TextField()
    eating_habbits = models.CharField(max_length=100)
    alcohol = models.CharField(max_length=10)
    smoke = models.CharField(max_length=10)
    other_habbit = models.CharField(max_length=100)
    legal_case = models.CharField(max_length=100)
    locChoice = models.CharField(max_length=100)
    ageGap = models.CharField(max_length=20)
    eduChoice = models.CharField(max_length=100)
    otherChoice = models.TextField()
    who = models.CharField(max_length=100)
    regMobile = models.CharField(max_length=20)
    resCat = models.CharField(max_length=50)
    nadi = models.CharField(max_length=50)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='divorce_sammelan_photos/')
    declaration = models.CharField(max_length=10)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Divorce Sammelan Registration"
        verbose_name_plural = "Divorce Sammelan Registrations"

class PhysicalForm(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=20)
    marital = models.CharField(max_length=50)
    disability = models.TextField(blank=True)
    tob = models.CharField(max_length=20, blank=True)
    birthPlace = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    visa = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=10, blank=True)
    weight = models.CharField(max_length=10, blank=True)
    education = models.CharField(max_length=100, blank=True)
    educationDetail = models.CharField(max_length=200, blank=True)
    occupationCat = models.CharField(max_length=100, blank=True)
    occupationDetails = models.TextField(blank=True)
    salary = models.CharField(max_length=20, blank=True)
    shani = models.CharField(max_length=30, blank=True)
    hobbies = models.CharField(max_length=200, blank=True)
    father = models.CharField(max_length=100, blank=True)
    mother = models.CharField(max_length=100, blank=True)
    fatherWp = models.CharField(max_length=20, blank=True)
    motherWp = models.CharField(max_length=20, blank=True)
    caste = models.CharField(max_length=100, blank=True)
    gotra = models.CharField(max_length=100, blank=True)
    kuldevi = models.CharField(max_length=100, blank=True)
    siblings = models.TextField(blank=True)
    eating_habbits = models.CharField(max_length=100, blank=True)
    alcohol = models.CharField(max_length=10, blank=True)
    smoke = models.CharField(max_length=10, blank=True)
    other_habbit = models.CharField(max_length=100, blank=True)
    legal_case = models.CharField(max_length=100, blank=True)
    locChoice = models.CharField(max_length=100, blank=True)
    ageGap = models.CharField(max_length=20, blank=True)
    eduChoice = models.CharField(max_length=100, blank=True)
    otherChoice = models.TextField(blank=True)
    who = models.CharField(max_length=100, blank=True)
    regMobile = models.CharField(max_length=20)
    resCat = models.CharField(max_length=50, blank=True)
    nadi = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='physical_form_photos/', blank=True)
    declaration = models.CharField(max_length=10)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Physical Form Registration"
        verbose_name_plural = "Physical Form Registrations"


# Bhudev Kalakaar 2026 - Talent Event Registration
class BhudevKalakaar2026Registration(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    AGE_GROUP_CHOICES = [
        ('5-10', '5 Yrs to 10 Yrs'),
        ('11-20', '11 Yrs to 20 Yrs'),
        ('21-40', '21 Yrs to 40 Yrs'),
        ('41-above', '41 Yrs and Above'),
    ]
    
    EVENT_CHOICES = [
        ('singing', 'Singing'),
        ('dancing', 'Dancing'),
        ('musical-instrument', 'Musical Instrument'),
        ('others', 'Others'),
    ]
    
    TERMS_CHOICES = [
        ('yes', 'Yes, I Agree'),
        ('no', "No, I Don't Agree"),
    ]
    
    # Personal Information
    fullName = models.CharField(max_length=200, verbose_name='Full Name of Participant')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='Gender')
    dateOfBirth = models.CharField(max_length=10, verbose_name='Date of Birth (DD-MM-YYYY)')
    ageGroup = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES, verbose_name='Age Group')
    
    # Event Information
    event = models.CharField(max_length=50, choices=EVENT_CHOICES, verbose_name='Event Category')
    talent = models.CharField(max_length=500, verbose_name='Talent Details', help_text='Mention details about your talent (e.g., Which Instrument, Awards, etc.)')
    
    # Contact Information
    city = models.CharField(max_length=100, verbose_name='Current Residence City')
    whatsappNumber = models.CharField(max_length=20, verbose_name='WhatsApp Number')
    
    # Photo
    photo = models.ImageField(upload_to='bk2026_registration_photos/', verbose_name='Participant Photo')
    
    # Terms & Conditions
    terms = models.CharField(max_length=10, choices=TERMS_CHOICES, verbose_name='Terms & Conditions Agreement')
    
    # Metadata
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name='Submission Date')
    
    class Meta:
        verbose_name = "Bhudev Kalakaar 2026 Talent Registration"
        verbose_name_plural = "Bhudev Kalakaar 2026 Talent Registrations"
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"{self.fullName} - {self.event} ({self.submitted_at.strftime('%Y-%m-%d')})"
