from django import forms
from .models import BncBnfApplication

class BncBnfApplicationForm(forms.ModelForm):
    class Meta:
        model = BncBnfApplication
        fields = '__all__'
