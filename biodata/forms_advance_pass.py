from django import forms
from .models import AdvancePassBooking

class AdvancePassBookingForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        entry_token_quantity = cleaned_data.get('entry_token_quantity', 0)
        unlimited_buffet_quantity = cleaned_data.get('unlimited_buffet_quantity', 0)
        cleaned_data['total_amount'] = entry_token_quantity * 50 + unlimited_buffet_quantity * 200
        return cleaned_data

    class Meta:
        model = AdvancePassBooking
        fields = [
            'name',
            'city',
            'whatsapp_number',
            'email',
            'entry_token_quantity',
            'unlimited_buffet_quantity',
            'payment_screenshot',
            'total_amount',
        ]
        widgets = {
            'total_amount': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
