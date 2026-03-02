from django import forms
from .models import StageRegistration

class StageRegistrationForm(forms.ModelForm):
    class Meta:
        model = StageRegistration
        fields = ['name_of_candidate', 'gender', 'dob', 'current_city', 'whatsapp_number']
        labels = {
            'name_of_candidate': 'Full Name of Candidate',
            'gender': 'Gender',
            'dob': 'Date Of Birth',
            'current_city': 'Current City',
            'whatsapp_number': 'WhatsApp Number',
        }
