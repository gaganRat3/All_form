from django import forms
from .models_karmkand_directory import GlobalKarmkandDirectoryEntry

class GlobalKarmkandDirectoryForm(forms.ModelForm):
    class Meta:
        model = GlobalKarmkandDirectoryEntry
        fields = [
            'name', 'dob', 'location', 'phone1', 'phone2',
                'brahman_activities', 'experience_years', 'other_skills',
                'service_level', 'employment_status',
                'photo', 'visiting_card', 'terms_agreed'
        ]
        widgets = {
            'dob': forms.TextInput(attrs={'placeholder': 'DD-MM-YYYY or as text'}),
                'brahman_activities': forms.HiddenInput(),
                'service_level': forms.HiddenInput(),
                'employment_status': forms.HiddenInput(),
                'terms_agreed': forms.CheckboxInput(),
        }
