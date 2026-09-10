from django import forms
from .models import AdvancePassBooking, AdvanceEntryPassBooking, AdvanceBuffetLunchBooking

class AdvanceEntryPassBookingForm(forms.ModelForm):
    """Dedicated form for Rs 50 (Entry + Tea Coffee) Pass."""
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'value': '1', 'id': 'id_quantity'}),
        label="Pass Quantity"
    )
    total_amount = forms.DecimalField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    class Meta:
        model = AdvanceEntryPassBooking
        fields = [
            'name',
            'city',
            'whatsapp_number',
            'email',
            'attend_city',
            'quantity',
            'payment_screenshot',
            'total_amount',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter WhatsApp number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'total_amount': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        qty = cleaned_data.get('quantity') or 1
        cleaned_data['quantity'] = qty
        cleaned_data['total_amount'] = qty * 50
        return cleaned_data


class AdvanceBuffetLunchBookingForm(forms.ModelForm):
    """Dedicated form for Rs 200 Unlimited Buffet Lunch Pass."""
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'value': '1', 'id': 'id_quantity'}),
        label="Buffet Lunch Quantity"
    )
    total_amount = forms.DecimalField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    class Meta:
        model = AdvanceBuffetLunchBooking
        fields = [
            'name',
            'city',
            'whatsapp_number',
            'email',
            'attend_city',
            'quantity',
            'payment_screenshot',
            'total_amount',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter WhatsApp number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'total_amount': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        qty = cleaned_data.get('quantity') or 1
        cleaned_data['quantity'] = qty
        cleaned_data['total_amount'] = qty * 200
        return cleaned_data


# Legacy combined form preserved for compatibility
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
            'attend_city',
            'entry_token_quantity',
            'unlimited_buffet_quantity',
            'payment_screenshot',
            'total_amount',
        ]
        widgets = {
            'total_amount': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
