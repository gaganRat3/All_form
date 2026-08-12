from django.contrib import admin

from .admin_38th_sammelan import Sammelan38BiodataAdmin
from .models_nri_sammelan import NriSammelanBiodata


@admin.register(NriSammelanBiodata)
class NriSammelanBiodataAdmin(Sammelan38BiodataAdmin):
    pass