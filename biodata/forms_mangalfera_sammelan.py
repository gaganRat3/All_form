from django import forms
from .models_mangalfera_sammelan import MangalferaSammelanBiodata


class MangalferaSammelanBiodataForm(forms.ModelForm):
    class Meta:
        model = MangalferaSammelanBiodata
        fields = '__all__'

