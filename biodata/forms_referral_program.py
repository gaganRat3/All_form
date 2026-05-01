from django import forms
from .models_referral_program import ReferralProgram

class ReferralProgramForm(forms.ModelForm):
    candidate_gender = forms.ChoiceField(
        choices=ReferralProgram.GENDER_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

    candidate_dob = forms.DateField(
        input_formats=["%d-%m-%Y", "%d/%m/%Y"],
        widget=forms.TextInput(
            attrs={
                "placeholder": "DD-MM-YYYY",
                "inputmode": "numeric",
                "autocomplete": "bday",
            }
        ),
        error_messages={"invalid": "Enter date as DD-MM-YYYY."},
        required=True,
    )

    class Meta:
        model = ReferralProgram
        fields = [
            'name', 'city', 'candidate_name', 'candidate_gender', 'candidate_dob',
            'mobile_no', 'whatsapp_no'
        ]

    def clean_candidate_dob(self):
        dob = self.cleaned_data['candidate_dob']
        import datetime
        if isinstance(dob, str):
            try:
                # Accept DD-MM-YYYY or DD/MM/YYYY
                dob = datetime.datetime.strptime(dob, "%d-%m-%Y").date()
            except ValueError:
                try:
                    dob = datetime.datetime.strptime(dob, "%d/%m/%Y").date()
                except ValueError:
                    raise forms.ValidationError("Enter date as DD-MM-YYYY.")
        return dob
