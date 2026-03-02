from django import forms
from .models import AudienceRegistration

class AudienceRegistrationForm(forms.ModelForm):
    class Meta:
        model = AudienceRegistration
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'ticket_quantity', 'total_amount', 'payment_screenshot']
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
                'placeholder': 'Enter your email address',
                'required': True
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
                'required': True
            }),
            'ticket_quantity': forms.NumberInput(attrs={
                'class': 'quantity-input',
                'min': 1,
                'max': 10,
                'value': 1
            }),
            'total_amount': forms.HiddenInput(),
            'payment_screenshot': forms.FileInput(attrs={
                'class': 'file-input',
                'accept': 'image/*,.pdf'
            })
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'ticket_quantity': 'Ticket Quantity',
            'total_amount': 'Total Amount',
            'payment_screenshot': 'Payment Screenshot',
        }

    def clean_ticket_quantity(self):
        quantity = self.cleaned_data.get('ticket_quantity')
        if quantity and (quantity < 1 or quantity > 10):
            raise forms.ValidationError("Ticket quantity must be between 1 and 10")
        return quantity

    def clean_total_amount(self):
        total_amount = self.cleaned_data.get('total_amount')
        ticket_quantity = self.cleaned_data.get('ticket_quantity', 1)
        expected_amount = ticket_quantity * 50.00
        
        if total_amount and abs(float(total_amount) - expected_amount) > 0.01:
            raise forms.ValidationError("Total amount doesn't match ticket quantity")
        return total_amount