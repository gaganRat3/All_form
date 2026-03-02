from django import forms
from .models_technical_support import TechnicalSupportRequest

class TechnicalSupportForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'input-focus w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500',
            'placeholder': 'Enter your first name',
            'id': 'firstName'
        })
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'input-focus w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500',
            'placeholder': 'Enter your last name',
            'id': 'lastName'
        })
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'input-focus w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500',
            'placeholder': 'Enter your city',
            'id': 'city'
        })
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'input-focus w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500',
            'placeholder': 'Enter your phone number',
            'id': 'phone'
        })
    )
    whatsapp_number = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input-focus w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500',
            'placeholder': 'Enter your WhatsApp number (optional)',
            'id': 'whatsappNumber'
        })
    )
    category = forms.CharField(
        widget=forms.HiddenInput(attrs={'id': 'issueCategory'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'input-focus w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:border-purple-500 resize-none',
            'rows': 5,
            'placeholder': 'Please provide detailed information about your issue...',
            'id': 'description'
        })
    )
    
    class Meta:
        model = TechnicalSupportRequest
        fields = ['first_name', 'last_name', 'city', 'phone', 'whatsapp_number', 'category', 'description']
