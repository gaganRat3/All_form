from django import forms
from django.core.validators import FileExtensionValidator
from .models_karmkand_directory import GlobalKarmkandDirectoryEntry

class GlobalKarmkandDirectoryForm(forms.ModelForm):
    """Enhanced form for Global Karmkand Directory registration"""
    
    # Checkbox fields for multiple selections
    BRAHMAN_ACTIVITIES_CHOICES = [
        ('wedding_puja', 'Wedding Puja'),
        ('house_warming', 'House Warming Puja'),
        ('satyanarayan', 'Satyanarayan Puja'),
        ('griha_pravesh', 'Griha Pravesh Puja'),
        ('mundan', 'Mundan Ceremony'),
        ('namkaran', 'Namkaran Ceremony'),
        ('antim_sanskar', 'Antim Sanskar'),
        ('havan', 'Havan/Yagya'),
        ('rudrabhishek', 'Rudrabhishek'),
        ('ganesh_puja', 'Ganesh Puja'),
        ('navgrah_shanti', 'Navgrah Shanti'),
        ('vastu_shanti', 'Vastu Shanti'),
        ('other', 'Other Pujas'),
    ]
    
    SERVICE_LEVEL_CHOICES = [
        ('local', 'Local Services Only'),
        ('regional', 'Regional Services'),
        ('national', 'National Services'),
        ('international', 'International Services'),
    ]
    
    EMPLOYMENT_STATUS_CHOICES = [
        ('full_time', 'Full Time Brahman'),
        ('part_time', 'Part Time Brahman'),
        ('freelance', 'Freelance Brahman'),
        ('temple_affiliated', 'Temple Affiliated'),
        ('independent', 'Independent Practitioner'),
    ]
    
    brahman_activities = forms.MultipleChoiceField(
        choices=BRAHMAN_ACTIVITIES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-checkbox h-4 w-4 text-blue-600 rounded'}),
        required=True,
        label="Brahman Activities/Specializations"
    )
    
    service_level = forms.MultipleChoiceField(
        choices=SERVICE_LEVEL_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-checkbox h-4 w-4 text-blue-600 rounded'}),
        required=True,
        label="Service Level Preferences"
    )
    
    employment_status = forms.MultipleChoiceField(
        choices=EMPLOYMENT_STATUS_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-checkbox h-4 w-4 text-blue-600 rounded'}),
        required=True,
        label="Employment Status"
    )
    
    class Meta:
        model = GlobalKarmkandDirectoryEntry
        fields = [
            'name', 'dob', 'location', 'address', 'phone1', 'phone2',
            'email', 'whatsapp', 'brahman_activities', 'experience_years',
            'other_skills', 'languages_known', 'service_level', 'employment_status',
            'photo', 'visiting_card', 'terms_agreed'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your full name'
            }),
            'dob': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'DD/MM/YYYY',
                'type': 'date'
            }),
            'location': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your city/location'
            }),
            'address': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 3,
                'placeholder': 'Enter your complete address'
            }),
            'phone1': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Primary phone number',
                'type': 'tel'
            }),
            'phone2': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Secondary phone number (optional)',
                'type': 'tel'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Email address (optional)'
            }),
            'whatsapp': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'WhatsApp number (optional)',
                'type': 'tel'
            }),
            'experience_years': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'min': 0,
                'max': 100,
                'placeholder': 'Years of experience'
            }),
            'other_skills': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 3,
                'placeholder': 'Any other skills, qualifications, or specializations'
            }),
            'languages_known': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Languages you can speak (comma separated)'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'accept': 'image/*'
            }),
            'visiting_card': forms.FileInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'accept': '.pdf,.jpg,.jpeg,.png'
            }),
            'terms_agreed': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded'
            })
        }
    
    def clean_brahman_activities(self):
        activities = self.cleaned_data.get('brahman_activities', [])
        return ','.join(activities)
    
    def clean_service_level(self):
        service_levels = self.cleaned_data.get('service_level', [])
        return ','.join(service_levels)
    
    def clean_employment_status(self):
        employment_statuses = self.cleaned_data.get('employment_status', [])
        return ','.join(employment_statuses)
    
    def clean_phone1(self):
        phone = self.cleaned_data.get('phone1')
        if phone:
            # Remove spaces and special characters
            phone = ''.join(filter(str.isdigit, phone))
            if len(phone) < 10:
                raise forms.ValidationError("Please enter a valid 10-digit phone number")
        return phone
    
    def clean_phone2(self):
        phone = self.cleaned_data.get('phone2')
        if phone:
            phone = ''.join(filter(str.isdigit, phone))
            if len(phone) < 10:
                raise forms.ValidationError("Please enter a valid 10-digit phone number")
        return phone
    
    def clean_whatsapp(self):
        whatsapp = self.cleaned_data.get('whatsapp')
        if whatsapp:
            whatsapp = ''.join(filter(str.isdigit, whatsapp))
            if len(whatsapp) < 10:
                raise forms.ValidationError("Please enter a valid 10-digit WhatsApp number")
        return whatsapp
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            if photo.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("Photo size should not exceed 5MB")
        return photo
    
    def clean_visiting_card(self):
        visiting_card = self.cleaned_data.get('visiting_card')
        if visiting_card:
            if visiting_card.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("File size should not exceed 5MB")
        return visiting_card
    
    def clean(self):
        cleaned_data = super().clean()
        terms_agreed = cleaned_data.get('terms_agreed')
        
        if not terms_agreed:
            raise forms.ValidationError("You must agree to the terms and conditions")
        
        return cleaned_data
