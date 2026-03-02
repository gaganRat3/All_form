from django import forms
from .models import SpotAdvanceBookletBooking

class AdvanceBookletBookingForm(forms.ModelForm):
    class Meta:
        model = SpotAdvanceBookletBooking
        fields = [
            'name',
            'city',
            'whatsapp_number',
            'email',
            'saurashtra_booklet',
            'gujarat_girls_booklet',
            'gujarat_boys_booklet',
            'nri_booklet',
            'mumbai_booklet',
            'divorce_widow_booklet',
            'payment_screenshot',
            'booklet_camp_city',
            'candidate_name_dob',
            # Removed 'total_amount' from fields as it is calculated in backend
        ]
        widgets = {
            'booklet_camp_city': forms.TextInput(attrs={'placeholder': 'Select Booklet Camp City'}),
            'candidate_name_dob': forms.TextInput(attrs={'placeholder': 'Enter Candidate Name & Date of Birth'}),
            # Removed total_amount widget since field removed
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        required_fields = ['name', 'city', 'whatsapp_number', 'email', 'payment_screenshot']
        for field_name in self.fields:
            self.fields[field_name].required = field_name in required_fields

    def clean(self):
        cleaned_data = super().clean()
        booklet_fields = [
            'saurashtra_booklet',
            'gujarat_girls_booklet',
            'gujarat_boys_booklet',
            'nri_booklet',
            'mumbai_booklet',
            'divorce_widow_booklet'
        ]
        selected = 0
        total = 0
        price_per_booklet = 500
        for field in booklet_fields:
            if cleaned_data.get(field):
                total += price_per_booklet
                selected += 1
        if selected == 0:
            raise forms.ValidationError("Please select at least one booklet type.")
        cleaned_data['total_amount'] = total
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # instance.with_courier = True  # Remove this as with_courier field does not exist
        # Set total_amount from cleaned_data calculated value
        if 'total_amount' in self.cleaned_data:
            instance.total_amount = self.cleaned_data['total_amount']
        if commit:
            instance.save()
        return instance
