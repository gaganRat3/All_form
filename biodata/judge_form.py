from django import forms
from .models import Judge

class JudgeForm(forms.ModelForm):
    expertise = forms.MultipleChoiceField(
        choices=Judge.EXPERTISE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    availability = forms.MultipleChoiceField(
        choices=Judge.AVAILABILITY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    terms = forms.ChoiceField(
        choices=Judge.TERMS_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    class Meta:
        model = Judge
        fields = [
            'full_name', 'email', 'phone', 'city',
            'expertise', 'experience', 'bio', 'availability',
            'photo', 'terms'
        ]

    def clean_expertise(self):
        expertise = self.cleaned_data.get('expertise')
        return ",".join(expertise)

    def clean_availability(self):
        availability = self.cleaned_data.get('availability')
        return ",".join(availability)
