from django import forms
from .models_business_directory import BusinessDirectoryEntry

class BusinessDirectoryForm(forms.ModelForm):
    def clean_website(self):
        website = self.cleaned_data.get('website')
        if website is None:
            website = ''
        website = website.strip()
        if not website:
            return ''
        if not website.startswith(('http://', 'https://')):
            website = 'http://' + website
        return website
    class Meta:
        model = BusinessDirectoryEntry
        fields = [
            'ownerName', 'businessName', 'services',
            'businessSegment', 'service_locations', 'address',
            'phone', 'whatsapp', 'email', 'website',
            'logo', 'ownerPhoto'
        ]
        widgets = {
            'services': forms.Textarea(attrs={'rows': 3}),
        }
