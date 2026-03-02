from django import forms
from .models import MegaBookletCorrectionRequest

class MegaBookletCorrectionForm(forms.ModelForm):
    class Meta:
        model = MegaBookletCorrectionRequest
        fields = [
            'candidate_name',
            'dob',
            'city',
            'whatsapp_number',
            'booklet_serial',
            'booklet_name',
            'correction_description',
            'photo_upload',
        ]
        labels = {
            'candidate_name': 'Candidate Name',
            'dob': 'Date of Birth',
            'city': 'City',
            'whatsapp_number': 'WhatsApp Number',
            'booklet_serial': 'Booklet Serial Number',
            'booklet_name': 'Booklet Name',
            'correction_description': 'Correction Request Description',
            'photo_upload': 'Photo Upload (optional)',
        }
        widgets = {
            'correction_description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(MegaBookletCorrectionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'photo_upload':
                field.required = True
            else:
                field.required = False
