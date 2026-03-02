from django import forms
from .models import GarbaPassRegistration

class GarbaPassRegistrationForm(forms.ModelForm):
    date_of_birth = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'DD-MM-YYYY', 'maxlength': '10'}))

    class Meta:
        model = GarbaPassRegistration
        fields = ['full_name', 'date_of_birth', 'residence_city', 'whatsapp_number', 'passes', 'subtotal', 'payment_screenshot']
        labels = {
            'full_name': 'Full Name',
            'date_of_birth': 'Date of Birth',
            'residence_city': 'Residence City',
            'whatsapp_number': 'WhatsApp Number',
            'passes': 'Passes (type, quantity, amount)',
            'subtotal': 'Subtotal',
            'payment_screenshot': 'Payment Screenshot',
        }

    class Media:
        js = ('js/date_mask.js',)
