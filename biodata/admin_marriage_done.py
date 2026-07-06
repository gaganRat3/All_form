import csv

from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html

from .models_marriage_done import MarriageDoneGiftSubmission


@admin.register(MarriageDoneGiftSubmission)
class MarriageDoneGiftSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'filler_name', 'relation', 'mobile', 'candidate_name', 'gender', 'candidate_dob',
        'spouse_name', 'spouse_dob', 'photo_preview', 'submitted_at'
    )
    search_fields = ('filler_name', 'relation', 'mobile', 'candidate_name', 'spouse_name')
    list_filter = ('gender', 'submitted_at')
    readonly_fields = ('submitted_at', 'photo_preview')
    date_hierarchy = 'submitted_at'
    actions = ['export_as_csv']

    def photo_preview(self, obj):
        if obj.wedding_photo:
            return format_html('<img src="{}" style="max-height: 90px; max-width: 90px; border-radius: 8px;" />', obj.wedding_photo.url)
        return '-'
    photo_preview.short_description = 'Wedding Photo'

    @admin.action(description='Export selected submissions to CSV')
    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=marriage_done_submissions.csv'
        writer = csv.writer(response)
        writer.writerow([
            'Filler Name', 'Relation', 'Mobile', 'Candidate Name', 'Gender', 'Candidate DOB',
            'Spouse Name', 'Spouse DOB', 'Wedding Photo', 'Submitted At'
        ])
        for obj in queryset:
            writer.writerow([
                obj.filler_name,
                obj.relation,
                obj.mobile,
                obj.candidate_name,
                obj.gender,
                obj.candidate_dob.strftime('%Y-%m-%d') if obj.candidate_dob else '',
                obj.spouse_name,
                obj.spouse_dob.strftime('%Y-%m-%d') if obj.spouse_dob else '',
                obj.wedding_photo.name if obj.wedding_photo else '',
                obj.submitted_at.strftime('%Y-%m-%d %H:%M:%S') if obj.submitted_at else '',
            ])
        return response
