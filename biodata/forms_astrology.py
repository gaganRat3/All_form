from django import forms

class AstrologyForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    whatsapp = forms.CharField(max_length=20, required=True)
    city = forms.CharField(max_length=100, required=True)
    candidateName = forms.CharField(max_length=100, required=True)
    candidateDOB = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Enter Candidate DOB as text'}))
    candidateBirthTime = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 1, 'placeholder': 'Enter Candidate Birth Time as text'}))
    candidateBirthPlace = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
