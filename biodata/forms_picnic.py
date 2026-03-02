from django import forms
from .models_picnic import PicnicRegistration
from datetime import datetime

class PicnicRegistrationForm(forms.ModelForm):
    dob = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'DD-MM-YYYY'})
    )
    
    class Meta:
        model = PicnicRegistration
        fields = '__all__'
    
    def clean_dob(self):
        dob_str = self.cleaned_data.get('dob')
        if dob_str:
            try:
                # Parse DD-MM-YYYY format
                dob = datetime.strptime(dob_str, '%d-%m-%Y').date()
                return dob
            except ValueError:
                raise forms.ValidationError('Please enter date in DD-MM-YYYY format')
        return dob_str
