from django.contrib import admin
from django.utils.html import format_html
from .models import Submission


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    """
    Admin configuration for Submission model.
    Shows an inline image thumbnail in the list view.
    """
    list_display  = ('name', 'email', 'city', 'image_preview', 'created_at')
    list_filter   = ('city', 'created_at')
    search_fields = ('name', 'email', 'city')
    readonly_fields = ('image_preview', 'created_at')

    def image_preview(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" style="height:60px; width:60px; object-fit:cover; '
                'border-radius:8px; border:1px solid #ddd;" />',
                obj.profile_image.url
            )
        return '—'
    image_preview.short_description = 'Photo'
