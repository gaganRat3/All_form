import io
import openpyxl
from openpyxl.utils import get_column_letter
from django.contrib import admin
from django.http import HttpResponse

from .models_diwali_gift import DiwaliGiftRegistration


@admin.register(DiwaliGiftRegistration)
class DiwaliGiftRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'serial_number',
        'candidate_name',
        'dob',
        'current_city',
        'candidate_mobile',
        'parents_mobile',
        'contact_person',
        'address',
        'contact_mobile',
        'pincode',
        'submitted_at',
    )
    search_fields = (
        'candidate_name',
        'current_city',
        'candidate_mobile',
        'parents_mobile',
        'contact_person',
        'contact_mobile',
        'pincode',
        'address',
    )
    list_filter = ('current_city', 'submitted_at')
    readonly_fields = ('submitted_at',)
    ordering = ['-submitted_at']
    actions = ['export_selected_to_excel']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('submitted_at')

    def serial_number(self, obj):
        request = getattr(self, 'admin_view_request', None)
        if request is None:
            return '-'
        queryset = self.get_queryset(request)
        pk_list = list(queryset.values_list('pk', flat=True))
        try:
            return pk_list.index(obj.pk) + 1
        except ValueError:
            return '-'
    serial_number.short_description = 'Serial No.'
    serial_number.admin_order_field = None

    def get_changelist_instance(self, request):
        self.admin_view_request = request
        return super().get_changelist_instance(request)

    @admin.action(description="Export Selected to Excel")
    def export_selected_to_excel(self, request, queryset):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Diwali Gift Registrations"

        headers = [
            "Serial No.",
            "Candidate Name",
            "Date of Birth",
            "Current City",
            "Candidate Mobile",
            "Parents Mobile",
            "Contact Person",
            "Delivery Address",
            "Courier Mobile",
            "Pincode",
            "Submitted At",
        ]
        ws.append(headers)

        export_queryset = self.get_queryset(request)
        pk_list = list(export_queryset.values_list('pk', flat=True))
        selected_ids = set(queryset.values_list('pk', flat=True))
        export_objs = [obj for obj in export_queryset if obj.pk in selected_ids]

        for obj in export_objs:
            try:
                serial_no = pk_list.index(obj.pk) + 1
            except ValueError:
                serial_no = '-'

            ws.append([
                serial_no,
                obj.candidate_name,
                obj.dob,
                obj.current_city,
                obj.candidate_mobile,
                obj.parents_mobile,
                obj.contact_person,
                obj.address,
                obj.contact_mobile,
                obj.pincode,
                obj.submitted_at.strftime('%Y-%m-%d %H:%M:%S') if obj.submitted_at else '',
            ])

        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = max(max_len + 3, 12)

        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response['Content-Disposition'] = 'attachment; filename=diwali_gift_registrations.xlsx'
        wb.save(response)
        return response
