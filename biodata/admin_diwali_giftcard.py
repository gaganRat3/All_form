import io
import openpyxl
from openpyxl.utils import get_column_letter
from django.contrib import admin
from django.http import HttpResponse

from .models_diwali_giftcard import DiwaliGiftCard


@admin.register(DiwaliGiftCard)
class DiwaliGiftCardAdmin(admin.ModelAdmin):
    list_display = (
        'serial_number',
        'candidate_name',
        'website_name',
        'membership_id',
        'whatsapp_number',
        'mobile_number',
        'home_address',
        'submitted_at',
    )
    search_fields = (
        'candidate_name',
        'website_name',
        'membership_id',
        'whatsapp_number',
        'mobile_number',
        'home_address',
    )
    list_filter = ('website_name', 'submitted_at')
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
        ws.title = "Diwali Gift Cards"

        headers = [
            "Serial No.",
            "Candidate Name",
            "Website Name",
            "Membership ID",
            "WhatsApp Number",
            "Mobile Number",
            "Home Address",
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
                obj.website_name,
                obj.membership_id,
                obj.whatsapp_number,
                obj.mobile_number,
                obj.home_address,
                obj.submitted_at.strftime('%Y-%m-%d %H:%M:%S') if obj.submitted_at else '',
            ])

        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = max(max_len + 4, 14)

        buffer = io.BytesIO()
        wb.save(buffer)
        buffer.seek(0)

        response = HttpResponse(
            buffer.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = 'attachment; filename="diwali_gift_card_registrations.xlsx"'
        return response

