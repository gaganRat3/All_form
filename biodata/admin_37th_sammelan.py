from django.contrib import admin
from .models_37th_sammelan import Sammelan37MumbaiMaharashtra

@admin.register(Sammelan37MumbaiMaharashtra)
class Sammelan37MumbaiMaharashtraAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'gender', 'dob', 'marital', 'disability', 'tob', 'birthPlace', 'city', 'country', 'visa',
        'height', 'weight', 'education', 'educationDetail', 'occupationCat', 'occupationDetails', 'salary', 'shani', 'hobbies',
        'father', 'mother', 'fatherWp', 'motherWp', 'caste', 'gotra', 'kuldevi', 'siblings',
        'eating_habbits', 'alcohol', 'smoke', 'other_habbit', 'legal_case',
        'locChoice', 'ageGap', 'eduChoice', 'otherChoice',
        'who', 'regMobile', 'resCat', 'nadi', 'email', 'whatsapp', 'photo', 'declaration', 'created_at'
    )
    search_fields = ('name', 'city', 'country', 'email', 'whatsapp')
    list_filter = ('gender', 'marital', 'city', 'country')
