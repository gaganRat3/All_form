from django import forms
from .models import ZoomRegistration

class ZoomRegistrationForm(forms.ModelForm):
    class Meta:
        model = ZoomRegistration
        fields = ['name', 'whatsapp', 'city', 'screenshot']
