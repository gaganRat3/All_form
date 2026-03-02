from django import forms
from .models import ParticipantRegistration


class ParticipantRegistrationForm(forms.ModelForm):
    # Event choices
    EVENT_CHOICES = [
        ('Singing', 'Singing'),
        ('Dance', 'Dance'),
        ('Music Instrument', 'Music Instrument'),
        ('Others', 'Others'),
    ]
    
    # Override events field to use multiple checkboxes
    events = forms.MultipleChoiceField(
        choices=EVENT_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        error_messages={
            'required': 'Please select at least one event to participate in.'
        }
    )
    
    class Meta:
        model = ParticipantRegistration
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'events', 'payment_screenshot']
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name',
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
                'required': True
            }),
            'payment_screenshot': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'required': True
            }),
        }
        
        error_messages = {
            'first_name': {
                'required': 'First name is required.',
                'max_length': 'First name must be less than 100 characters.'
            },
            'last_name': {
                'required': 'Last name is required.',
                'max_length': 'Last name must be less than 100 characters.'
            },
            'email': {
                'required': 'Email is required.',
                'invalid': 'Please enter a valid email address.'
            },
            'phone_number': {
                'required': 'Phone number is required.',
                'max_length': 'Phone number must be less than 20 characters.'
            },
            'payment_screenshot': {
                'required': 'Payment screenshot is required.'
            }
        }
    
    def clean_events(self):
        """Custom validation for events field"""
        events = self.cleaned_data.get('events')
        if not events:
            raise forms.ValidationError('Please select at least one event to participate in.')
        return events
    
    def clean_phone_number(self):
        """Custom validation for phone number"""
        phone = self.cleaned_data.get('phone_number')
        if phone:
            # Remove any non-digit characters for validation
            digits_only = ''.join(filter(str.isdigit, phone))
            if len(digits_only) < 10:
                raise forms.ValidationError('Please enter a valid phone number with at least 10 digits.')
        return phone
    
    def save(self, commit=True):
        """Override save to calculate subtotal"""
        instance = super().save(commit=False)
        
        # Calculate subtotal (Rs 100 per event)
        events = self.cleaned_data.get('events', [])
        instance.subtotal = len(events) * 100
        
        if commit:
            instance.save()
        return instance