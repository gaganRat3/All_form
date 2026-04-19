
from django import forms

from .models import FlipBookAccessRegistration, StudentBookResaleRegistration

# Form for Flip-Book Access Registration
class FlipBookAccessRegistrationForm(forms.ModelForm):
    class Meta:
        model = FlipBookAccessRegistration
        fields = ['candidate_name', 'dob', 'gender', 'city', 'whatsapp', 'email']
        labels = {
            'candidate_name': 'Name of Candidate',
            'dob': 'Candidate Date of Birth',
            'gender': 'Candidate Gender',
            'city': 'Current City',
            'whatsapp': 'WhatsApp Number',
            'email': 'Email ID',
        }

# Form for 39th Sammelan Biodata
from .models import Sammelan39Biodata
class StudentBookResaleRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentBookResaleRegistration
        fields = [
            'student_name', 'father_name', 'mother_name', 'dob', 'gender', 'standard', 'school', 'board',
            'mother_whatsapp', 'father_whatsapp', 'area', 'contact_details', 'participate'
        ]
        labels = {
            'student_name': 'Student Name',
            'father_name': 'Father Name',
            'mother_name': 'Mother Name',
            'dob': 'Date of Birth',
            'gender': 'Gender',
            'standard': 'Std (Class)',
            'school': 'School',
            'board': 'Board',
            'mother_whatsapp': 'Mother WhatsApp Number',
            'father_whatsapp': 'Father WhatsApp Number',
            'area': 'Area / Locality',
            'contact_details': 'Contact Details (Address / Landmark / Email)',
            'participate': 'I want to participate',
        }

class Sammelan39BiodataForm(forms.ModelForm):
    class Meta:
        model = Sammelan39Biodata
        fields = '__all__'
        labels = {
            'name': 'Candidate Full Name',
            'gender': 'Gender',
            'dob': 'Date of Birth',
            'marital': 'Marital Status',
            'disability': 'Any Disability or Minor Problem?',
            'tob': 'Birth Time',
            'birthPlace': 'Birth Place',
            'city': 'Current City',
            'country': 'Current Country',
            'visa': 'Visa Status',
            'height': 'Height',
            'weight': 'Weight (kg)',
            'education': 'Education',
            'educationDetail': 'Education Detail',
            'occupationCat': 'Occupation Type',
            'occupationDetails': 'Company / Business Name',
            'salary': 'Monthly Income (Rs.)',
            'shani': 'Shani / Mangal',
            'hobbies': 'Hobbies',
            'father': "Father's Name",
            'mother': "Mother's Name",
            'fatherWp': "Father's Mobile No.",
            'motherWp': "Mother's Mobile No.",
            'caste': 'Type of Brahmin',
            'gotra': 'Gotra',
            'kuldevi': 'Kuldevi',
            'siblings': 'Siblings (Brother / Sister)',
            'eating_habbits': 'Eating Habits',
            'alcohol': 'Alcoholic Drinks?',
            'smoke': 'Smoke?',
            'other_habbit': 'Any Other Habit?',
            'legal_case': 'Any Legal or Police Case?',
            'locChoice': "Partner's Location",
            'ageGap': "Partner's Age Bracket",
            'eduChoice': "Partner's Education",
            'otherChoice': 'Any Other Specific Choice',
            'who': 'Who is doing this Registration?',
            'regMobile': 'Mobile No. (person registering)',
            'resCat': 'Current Residence Area',
            'nadi': 'Nadi',
            'email': 'Email Address',
            'whatsapp': 'WhatsApp Number',
            'photo': 'Upload Candidate Photo',
            'declaration': 'Declaration',
        }
# Ensure forms is imported for new form

# 40 Plus Sammelan Form
from .models import FortyPlusSammelan, SaurasthraKutchSammelan
from .models_37th_sammelan import Sammelan37MumbaiMaharashtra

class FortyPlusSammelanForm(forms.ModelForm):
    class Meta:
        model = FortyPlusSammelan
        fields = '__all__'


class Sammelan37MumbaiMaharashtraForm(forms.ModelForm):
    RESCAT_CHOICES = [
        ('gujarat_region', 'Gujarat Region (North or Central or South)'),
        ('saurashtra_region', 'Saurashtra Region'),
        ('kachchh_region', 'Kachchh Region'),
        ('mumbai_maharashtra', 'Mumbai & Maharashtra Region'),
        ('rest_of_india', 'Rest of Indian Region (except Gujarat & Maharashtra)'),
        ('nri', 'NRI (Any Visa)'),
    ]
    resCat = forms.ChoiceField(choices=RESCAT_CHOICES, required=True, label='Current Residence Area')
    class Meta:
        model = Sammelan37MumbaiMaharashtra
        fields = '__all__'


class SaurasthraKutchSammelanForm(forms.ModelForm):
    RESCAT_CHOICES = [
        ('saurashtra', 'Saurashtra Region'),
        ('kachchh', 'Kachchh Region'),
        ('nri', 'NRI (Any Visa)'),
    ]
    resCat = forms.ChoiceField(choices=RESCAT_CHOICES, required=True, label='Current Residence Area')
    class Meta:
        model = SaurasthraKutchSammelan
        fields = '__all__'

from django import forms
# Form for Booklet Library submissions
from .models import BookletLibrarySubmission

class BookletLibraryForm(forms.ModelForm):
    class Meta:
        model = BookletLibrarySubmission
        fields = ['name', 'dob', 'gender', 'city', 'whatsapp', 'email']
        labels = {
            'name': 'Candidate Name',
            'dob': 'Date of Birth',
            'gender': 'Gender',
            'city': 'Current City',
            'whatsapp': 'WhatsApp Number',
            'email': 'Email Address',
        }
        widgets = {
            'dob': forms.TextInput(attrs={'placeholder': 'DD-MM-YYYY'}),
            'gender': forms.RadioSelect(choices=[('male', 'Male'), ('female', 'Female')]),
        }
from django import forms
from .models import CandidateBiodata, MegaBookletCorrectionRequest, SammelanPaymentForm, AdvanceBookletBooking, CourierBooklet35thBooking
from .models import DivorceSammelanForm, PhysicalForm

class CandidateBiodataForm(forms.ModelForm):
    class Meta:
        model = CandidateBiodata
        fields = '__all__'
        labels = {
            'candidate_name': 'Name Of Candidate / ઉમેદવાર નું નામ',
            'dob': 'Date Of Birth',
            'birth_time': 'Time Of Birth',
            'birth_place': 'Birth Place',
            'height': 'Height (In Feet)',
            'weight': 'Weight (In KG)',
            'education': 'Highest Education Category',
            'education_details': 'Education',
            'occupation': 'Job/Business/Occupation Category',
            'occupation_details': 'Details on Job / Business / Occupation',
            'monthly_income': 'Salary (optional) Per Month Salary)',
            'partner_education': 'Choice Of Education (Partner Preference)',
            'partner_location': 'Choice Of Location (Partner Preference)',
            'partner_age_bracket': 'Choice Of Age Gap/ Difference in Year (Partner Preference)',
            'declaration': 'Declaration : હું અહીં ખાત્રી આપુ છું કે, મે ભરેલી, ઉપરોક્ત બધી માહિતી ખરી છે. સાચી છે, અને મે બધી માહિતી ચેક કરી લીધી છે. મારો બાયોડેટા લેટેસ્ટ બુકલેટ મા સમાવેશ કરશો. (I hereby declare that all above info filled by myself is correct & all right and i have checked all info before submission of this Form. Please include my Biodata in latest Biodata Booklet)',
            'declaration_agree': 'Agree (ઉપર મુજબ હું માનું છું અને તેમ કરીશ) - મારો બાયોડેટા બુકલેટ માં ચોક્કસ સમાવેશ કરશોજી',
            'declaration_disagree': 'Disagree (ઉપર મુજબ હું નહિ માનું)  - મારો બાયોડેટા કેન્સલ કરી દેજો',
            'gender': 'Candidate Gender',
            'registration_by': 'Who is doing this Registration ? (કોણ રેજીસ્ટ્રેશન કરી રહ્યું છે ? એ વિગત અહીં લખશો)   Example : SELF / Candidate\'s Father (Name) / Candidate\'s Mother (Name) /  Candidate\'s Brother (Name)  , etc',
            'registrant_mobile': 'જે આ રેજીસ્ટ્રેશન કરી રહ્યું છે , તે અહીં પોતાનો MOBILE નંબર લખશો // Mention here your own Mobile Number (for Reference & Verification Purpose)',
            'residence_area_category': 'Candidate Current Residence Area Category',
            'current_country': 'Candidate Current Country',
            'visa_status': 'Visa or Residence Status Of Candidate',
            'photograph': 'Upload 1 Candidate Photo (Photo Should be Clear visible front-face, Bright light on Face, No Goggles or Cap , Close-up photo or Passport Size Photo is required)',
            'mother_mobile': "Mother's Whatsapp Number",
            'father_mobile': "Father's Whatsapp Number",
            'whatsapp_number': "Whatsapp Number (For verification)",
            'kuldevi': 'Any Disability/ Details',
        }

class MegaBookletCorrectionForm(forms.ModelForm):
    class Meta:
        model = MegaBookletCorrectionRequest
        fields = [
            'candidate_name',
            'city',
            'whatsapp_number',
            'booklet_serial',
            'booklet_name',
            'correction_description',
        ]
        labels = {
            'candidate_name': 'Candidate Name',
            'city': 'City',
            'whatsapp_number': 'WhatsApp Number',
            'booklet_serial': 'Booklet Serial Number',
            'booklet_name': 'Booklet Name',
            'correction_description': 'Correction Request Description',
        }
        widgets = {
            'correction_description': forms.Textarea(attrs={'rows': 4}),
        }


class SammelanPaymentFormForm(forms.ModelForm):
    class Meta:
        model = SammelanPaymentForm
        fields = ['name', 'date_of_birth', 'mobile_number', 'marital_status', 'payment_screenshot']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
                'required': True
            }),
            'date_of_birth': forms.TextInput(attrs={
                'class': 'form-control dob-input',
                'placeholder': 'DD-MM-YYYY',
                'maxlength': '10',
                'required': True
            }),
            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your mobile number',
                'required': True
            }),
            'marital_status': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your marital status',
                'required': True
            }),
            'payment_screenshot': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'required': True
            }),
        }


# Divorce Sammelan Form
class DivorceSammelanFormForm(forms.ModelForm):
    class Meta:
        model = DivorceSammelanForm
        fields = '__all__'


# Courier Booklet Form (35th Event)
class CourierBooklet35thForm(forms.ModelForm):
    class Meta:
        model = CourierBooklet35thBooking
        fields = [
            'name',
            'city',
            'whatsapp_number',
            'email',
            'girls_booklet_with',
            'boys_booklet_with',
            'courier_address',
            'payment_screenshot',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your city'
            }),
            'whatsapp_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter WhatsApp number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'courier_address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter delivery address',
                'rows': 3
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        required_fields = ['name', 'city', 'whatsapp_number', 'email', 'payment_screenshot', 'courier_address']
        for field_name in self.fields:
            self.fields[field_name].required = field_name in required_fields

    def clean(self):
        cleaned_data = super().clean()
        girls_booklet_with = cleaned_data.get('girls_booklet_with')
        boys_booklet_with = cleaned_data.get('boys_booklet_with')
        courier_address = cleaned_data.get('courier_address')

        # At least one booklet type must be chosen
        if not (girls_booklet_with or boys_booklet_with):
            raise forms.ValidationError("Please select at least one booklet type (Girls/Boys).")

        # Courier address required
        if not courier_address:
            self.add_error('courier_address', 'Delivery address is required for courier service.')

        # Calculate total: ₹500 per booklet + ₹100 courier charge (if at least one selected)
        total = 0
        price_per_booklet = 500
        courier_charge = 100
        selected = 0
        if girls_booklet_with:
            total += price_per_booklet
            selected += 1
        if boys_booklet_with:
            total += price_per_booklet
            selected += 1
        if selected > 0:
            total += courier_charge
        cleaned_data['total_amount'] = total

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Set total_amount from cleaned_data calculated value
        if 'total_amount' in self.cleaned_data:
            instance.total_amount = self.cleaned_data['total_amount']
        if commit:
            instance.save()
        return instance


# Physical Form for Backend Implementation
class PhysicalFormForm(forms.ModelForm):
    class Meta:
        model = PhysicalForm
        fields = '__all__'
        labels = {
            'name': 'Candidate Name',
            'gender': 'Gender',
            'dob': 'Date of Birth',
            'marital': 'Marital Status',
            'disability': 'Any Disability or Minor Problem?',
            'tob': 'Birth Time',
            'birthPlace': 'Birth Place',
            'city': 'Current City',
            'country': 'Current Country',
            'visa': 'Visa Status',
            'height': 'Height',
            'weight': 'Weight (kg)',
            'education': 'Education',
            'educationDetail': 'Education Detail',
            'occupationCat': 'Occupation Type',
            'occupationDetails': 'Company / Business Name',
            'salary': 'Monthly Income (₹)',
            'shani': 'Shani / Mangal',
            'hobbies': 'Hobbies',
            'father': "Father's Name",
            'mother': "Mother's Name",
            'fatherWp': "Father's Mobile No.",
            'motherWp': "Mother's Mobile No.",
            'caste': 'Type of Brahmin',
            'gotra': 'Gotra',
            'kuldevi': 'Kuldevi',
            'siblings': 'Siblings (Brother/Sister)',
            'eating_habbits': 'Eating Habits',
            'alcohol': 'Alcoholic Drinks?',
            'smoke': 'Smoke?',
            'other_habbit': 'Any Other Habit?',
            'legal_case': 'Any Legal or Police Case?',
            'locChoice': "Partner's Location",
            'ageGap': "Partner's Age Bracket",
            'eduChoice': "Partner's Education",
            'otherChoice': 'Any Other Specific Choice',
            'who': 'Who is doing this Registration?',
            'regMobile': 'Mobile Number (of person registering)',
            'resCat': 'Current Residence Area',
            'nadi': 'Nadi',
            'email': 'Email Address',
            'whatsapp': 'WhatsApp Number',
            'photo': 'Upload Candidate Photo',
            'declaration': 'Declaration',
        }


# Bhudev Kalakaar 2026 Talent Registration Form
from .models import BhudevKalakaar2026Registration

class BhudevKalakaar2026Form(forms.ModelForm):
    class Meta:
        model = BhudevKalakaar2026Registration
        fields = ['fullName', 'gender', 'dateOfBirth', 'ageGroup', 'talent', 'city', 'whatsappNumber', 'photo', 'terms']
        labels = {
            'fullName': 'Full Name of the Participant',
            'gender': 'Gender (Male / Female)',
            'dateOfBirth': 'Date of Birth (DD-MM-YYYY)',
            'ageGroup': 'Age Group',
            'talent': 'Talent Details',
            'city': 'Current Residence City',
            'whatsappNumber': 'WhatsApp Number',
            'photo': 'Participant Photo',
            'terms': 'Terms & Conditions Agreement',
        }
        widgets = {
            'fullName': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name',
                'required': True
            }),
            'gender': forms.RadioSelect(choices=[('male', 'Male'), ('female', 'Female')]),
            'dateOfBirth': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'DD-MM-YYYY',
                'maxlength': '10',
                'required': True
            }),
            'ageGroup': forms.RadioSelect(),
            'talent': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter talent details',
                'required': True
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter city name',
                'required': True
            }),
            'whatsappNumber': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter WhatsApp number',
                'type': 'tel',
                'required': True
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'required': True
            }),
            'terms': forms.RadioSelect(choices=[('yes', 'Yes, I Agree'), ('no', "No, I Don't Agree")]),
        }


# Get-Together Registration Form
from .models import GetTogetherRegistration

class GetTogetherRegistrationForm(forms.ModelForm):
    dob = forms.DateField(
        input_formats=['%d-%m-%Y'],
        error_messages={'invalid': 'Please enter date in DD-MM-YYYY format.'}
    )

    class Meta:
        model = GetTogetherRegistration
        fields = ['candidate_name', 'gender', 'dob', 'city', 'whatsapp', 'members']
        labels = {
            'candidate_name': 'Candidate Name',
            'gender': 'Gender',
            'dob': 'Date of Birth',
            'city': 'Current City',
            'whatsapp': 'WhatsApp No.',
            'members': 'How many Members can attend this Program',
        }
