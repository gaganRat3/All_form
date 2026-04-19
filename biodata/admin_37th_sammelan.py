from django.contrib import admin
from .models_37th_sammelan import Sammelan37MumbaiMaharashtra

@admin.register(Sammelan37MumbaiMaharashtra)
class Sammelan37MumbaiMaharashtraAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'gender', 'dob', 'marital', 'disability', 'tob', 'birthPlace', 'city', 'country',
        'visa_display', 'height', 'weight', 'education', 'educationDetail', 'occupationCat',
        'occupationDetails', 'salary', 'shani', 'hobbies', 'father', 'mother', 'fatherWp',
        'motherWp', 'caste', 'gotra', 'kuldevi', 'siblings', 'eating_habbits', 'alcohol',
        'smoke', 'other_habbit', 'legal_case', 'locChoice', 'ageGap', 'eduChoice', 'otherChoice',
        'who', 'regMobile', 'residence_display', 'nadi_display', 'email', 'whatsapp', 'photo',
        'declaration', 'created_at'
    )
    search_fields = ('name', 'city', 'email', 'whatsapp', 'regMobile', 'father', 'mother', 'occupationCat')
    list_filter = ('gender', 'marital', 'resCat', 'visa', 'country', 'created_at')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 25
    
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

    @admin.display(description='Residence Area')
    def residence_display(self, obj):
        return obj.get_resCat_display()

    @admin.display(description='Visa Status')
    def visa_display(self, obj):
        return obj.get_visa_display()

    @admin.display(description='Nadi')
    def nadi_display(self, obj):
        return obj.get_nadi_display()
    
    @admin.action(description='Export selected registrations to CSV')
    def export_as_csv(self, request, queryset):
        """Export 37th Sammelan registrations to CSV format"""
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=37th_sammelan_uk_europe.csv'
        
        writer = csv.writer(response)
        # Write header
        writer.writerow([
            'Name', 'Gender', 'DOB', 'Marital Status', 'Disability', 'Birth Time', 'Birth Place',
            'City', 'Country', 'Visa Status', 'Height', 'Weight', 'Education', 'Education Detail',
            'Occupation Type', 'Occupation Details', 'Salary', 'Shani/Mangal', 'Hobbies',
            'Father Name', 'Father Mobile', 'Mother Name', 'Mother Mobile', 'Caste', 'Gotra',
            'Kuldevi', 'Siblings', 'Eating Habits', 'Alcohol', 'Smoke', 'Other Habit', 'Legal Case',
            'Partner Location Choice', 'Partner Age Gap', 'Partner Education Choice', 'Partner Other Choice',
            'Who Registered', 'Register Mobile', 'Residence Area', 'Nadi', 'Email', 'WhatsApp',
            'Declaration', 'Photo Path', 'Submitted Date'
        ])
        
        # Write data
        for registration in queryset:
            writer.writerow([
                registration.name,
                registration.gender,
                registration.dob,
                registration.get_marital_display(),
                registration.disability,
                registration.tob,
                registration.birthPlace,
                registration.city,
                registration.country,
                registration.get_visa_display(),
                registration.height,
                registration.weight,
                registration.education,
                registration.educationDetail,
                registration.occupationCat,
                registration.occupationDetails,
                registration.salary,
                registration.shani,
                registration.hobbies,
                registration.father,
                registration.fatherWp,
                registration.mother,
                registration.motherWp,
                registration.caste,
                registration.gotra,
                registration.kuldevi,
                registration.siblings,
                registration.eating_habbits,
                registration.alcohol,
                registration.smoke,
                registration.other_habbit,
                registration.legal_case,
                registration.locChoice,
                registration.ageGap,
                registration.eduChoice,
                registration.otherChoice,
                registration.who,
                registration.regMobile,
                registration.get_resCat_display(),
                registration.get_nadi_display(),
                registration.email,
                registration.whatsapp,
                registration.declaration,
                registration.photo.name if registration.photo else '',
                registration.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            ])
        
        return response
