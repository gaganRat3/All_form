from django import forms
from .models import DivorceSammelanRegistration

class DivorceSammelanRegistrationForm(forms.ModelForm):
    class Meta:
        model = DivorceSammelanRegistration
        fields = '__all__'
