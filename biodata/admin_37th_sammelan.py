from django.contrib import admin
from .models_37th_sammelan import Sammelan37MumbaiMaharashtra

@admin.register(Sammelan37MumbaiMaharashtra)
class Sammelan37MumbaiMaharashtraAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'gender', 'dob', 'email', 'whatsapp', 'resCat', 'created_at'
    )
    search_fields = ('name', 'city', 'email', 'whatsapp', 'father', 'mother')
    list_filter = ('gender', 'marital', 'resCat', 'visa', 'country', 'created_at')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Personal Details', {
            'fields': ('name', 'gender', 'dob', 'tob', 'birthPlace', 'marital', 'disability')
        }),
        ('Contact & Location', {
            'fields': ('city', 'country', 'visa', 'resCat')
        }),
        ('Physical Details', {
            'fields': ('height', 'weight')
        }),
        ('Professional Details', {
            'fields': ('education', 'educationDetail', 'occupationCat', 'occupationDetails', 'salary')
        }),
        ('Family Details', {
            'fields': ('father', 'fatherWp', 'mother', 'motherWp', 'caste', 'gotra', 'kuldevi', 'siblings')
        }),
        ('Lifestyle & Habits', {
            'fields': ('eating_habbits', 'alcohol', 'smoke', 'other_habbit', 'shani', 'hobbies', 'legal_case')
        }),
        ('Astrology', {
            'fields': ('nadi',)
        }),
        ('Partner Preferences', {
            'fields': ('locChoice', 'ageGap', 'eduChoice', 'otherChoice')
        }),
        ('Registration Details', {
            'fields': ('who', 'regMobile', 'email', 'whatsapp', 'photo', 'declaration')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['export_as_csv']
    
    @admin.action(description='Export selected registrations to CSV')
    def export_as_csv(self, request, queryset):
        """Export 37th Sammelan registrations to CSV format"""
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=37th_sammelan_mumbai_maharashtra.csv'
        
        writer = csv.writer(response)
        # Write header
        writer.writerow([
            'Name', 'Gender', 'DOB', 'Marital Status', 'Email', 'WhatsApp', 
            'City', 'Country', 'Residence Area', 'Visa Status', 'Occupation', 
            'Education', 'Father Name', 'Mother Name', 'Submitted Date'
        ])
        
        # Write data
        for registration in queryset:
            writer.writerow([
                registration.name,
                registration.gender,
                registration.dob,
                registration.get_marital_display(),
                registration.email,
                registration.whatsapp,
                registration.city,
                registration.country,
                registration.get_resCat_display(),
                registration.get_visa_display(),
                registration.occupationCat,
                registration.education,
                registration.father,
                registration.mother,
                registration.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            ])
        
        return response
