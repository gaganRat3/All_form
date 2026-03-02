from django.contrib import admin
from .models_karmkand_directory import GlobalKarmkandDirectoryEntry

@admin.register(GlobalKarmkandDirectoryEntry)
class GlobalKarmkandDirectoryEntryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'dob', 'location', 'phone1', 'phone2',
        'brahman_activities', 'experience_years', 'other_skills',
        'service_level', 'employment_status',
        'photo_preview', 'visiting_card', 'terms_agreed', 'submitted_at'
    )
    readonly_fields = ('photo_preview', 'submitted_at')
    search_fields = ('name', 'location', 'phone1', 'phone2')
    list_filter = ('service_level', 'employment_status', 'terms_agreed')

    actions = ['export_as_excel', 'download_images_zip']

    def photo_preview(self, obj):
        from django.utils.html import format_html
        if obj.photo:
            filename = obj.photo.name.split('/')[-1]
            return format_html('<a href="{}" target="_blank">{}</a>', obj.photo.url, filename)
        return "-"
    photo_preview.allow_tags = True
    photo_preview.short_description = "Photo Preview"

    def export_as_excel(self, request, queryset):
        import openpyxl
        from django.http import HttpResponse
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Karmkand Directory"
        headers = [
            'Name', 'DOB', 'Location', 'Phone1', 'Phone2', 'Brahman Activities',
            'Experience Years', 'Other Skills', 'Service Level', 'Employment Status',
            'Photo', 'Visiting Card', 'Terms Agreed', 'Submitted At'
        ]
        ws.append(headers)
        for obj in queryset:
            ws.append([
                obj.name, obj.dob, obj.location, obj.phone1, obj.phone2,
                obj.brahman_activities, obj.experience_years, obj.other_skills,
                obj.service_level, obj.employment_status,
                obj.photo.url if obj.photo else '',
                obj.visiting_card.url if obj.visiting_card else '',
                obj.terms_agreed, obj.submitted_at.strftime('%Y-%m-%d %H:%M:%S')
            ])
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=global_karmkand_directory.xlsx'
        wb.save(response)
        return response
    export_as_excel.short_description = "Export selected as Excel"

    def download_images_zip(self, request, queryset):
        import io
        import zipfile
        from django.http import HttpResponse
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for obj in queryset:
                if obj.photo:
                    photo_path = obj.photo.path
                    zip_file.write(photo_path, f"photos/{obj.photo.name.split('/')[-1]}")
                if obj.visiting_card:
                    card_path = obj.visiting_card.path
                    zip_file.write(card_path, f"visiting_cards/{obj.visiting_card.name.split('/')[-1]}")
        zip_buffer.seek(0)
        response = HttpResponse(zip_buffer, content_type="application/zip")
        response['Content-Disposition'] = 'attachment; filename=karmkand_images.zip'
        return response
    download_images_zip.short_description = "Download images as ZIP"
