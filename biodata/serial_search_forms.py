from django import forms

class SerialSearchForm(forms.Form):
    dob = forms.DateField(
        label='Enter Date Of Birth',
        input_formats=['%d-%m-%Y'],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'dd-mm-yyyy'})
    )
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = forms.ChoiceField(
        label='Select Gender',
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        initial=None
    )
