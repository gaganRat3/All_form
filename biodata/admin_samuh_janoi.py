import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from django.contrib import admin
from django.http import HttpResponse

from .models_samuh_janoi import SamuhJanoiRegistration


@admin.register(SamuhJanoiRegistration)
class SamuhJanoiRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'serial_number',
        'batuk_name',
        'batuk_dob',
        'father_name',
        'mother_name',
        'sub_caste',
        'gotra',
        'village_city',
        'phone_number',
        'whatsapp_number',
        'attending_members',
        'submitted_at',
    )
    search_fields = (
        'batuk_name',
        'father_name',
        'mother_name',
        'sub_caste',
        'gotra',
        'village_city',
        'home_address',
        'phone_number',
        'whatsapp_number',
        'extra_member_notes',
    )
    list_filter = (
        'sub_caste',
        'village_city',
        'submitted_at',
    )
    readonly_fields = ('submitted_at',)
    ordering = ['-submitted_at']
    actions = ['export_selected_to_excel']

    fieldsets = (
        ('બટુકની માહિતી (Batuk Details)', {
            'fields': ('batuk_name', 'batuk_dob')
        }),
        ('માતા-પિતાની માહિતી (Parents Details)', {
            'fields': ('father_name', 'mother_name')
        }),
        ('જ્ઞાતિ અને ગૌત્ર વિગત (Community & Gotra)', {
            'fields': ('sub_caste', 'gotra')
        }),
        ('સરનામું અને સંપર્ક (Address & Contact)', {
            'fields': ('home_address', 'village_city', 'phone_number', 'whatsapp_number')
        }),
        ('પ્રસંગમાં આવનાર સભ્યો (Attending Members)', {
            'fields': ('attending_members', 'extra_member_notes'),
            'description': 'મર્યાદા: ૩૦ સભ્યો. વધારાના સભ્યો માટે નોંધ.'
        }),
        ('સિસ્ટમ માહિતી (System Metadata)', {
            'fields': ('submitted_at',),
            'classes': ('collapse',)
        }),
    )

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

    serial_number.short_description = 'Sr. No.'
    serial_number.admin_order_field = None

    def get_changelist_instance(self, request):
        self.admin_view_request = request
        return super().get_changelist_instance(request)

    @admin.action(description="Export Selected to Excel (.xlsx)")
    def export_selected_to_excel(self, request, queryset):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Samuh Janoi Registrations"

        headers = [
            "Sr. No.",
            "બટુક નું પૂરું નામ",
            "જન્મ તારીખ",
            "પિતા નું નામ",
            "માતા નું નામ",
            "પેટા-જ્ઞાતિ",
            "ગૌત્ર",
            "ગામ / શહેર",
            "ફોન નંબર",
            "વોટ્સએપ નંબર",
            "ઘરનું સરનામું (પિનકોડ)",
            "આવનાર સભ્યો સંખ્યા",
            "વધારાના સભ્યો નોંધ",
            "રજીસ્ટ્રેશન તારીખ / સમય",
        ]
        ws.append(headers)

        header_font = Font(name='Calibri', size=11, bold=True, color='FFFFFF')
        header_fill = PatternFill(start_color='641C24', end_color='641C24', fill_type='solid')
        header_align = Alignment(horizontal='center', vertical='center', wrap_text=True)

        for col_idx in range(1, len(headers) + 1):
            cell = ws.cell(row=1, column=col_idx)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_align

        export_queryset = self.get_queryset(request)
        pk_list = list(export_queryset.values_list('pk', flat=True))
        selected_ids = set(queryset.values_list('pk', flat=True))
        export_objs = [obj for obj in export_queryset if obj.pk in selected_ids]

        thin_border = Border(
            left=Side(style='thin', color='E0E0E0'),
            right=Side(style='thin', color='E0E0E0'),
            top=Side(style='thin', color='E0E0E0'),
            bottom=Side(style='thin', color='E0E0E0'),
        )

        row_idx = 2
        for obj in export_objs:
            try:
                sr_no = pk_list.index(obj.pk) + 1
            except ValueError:
                sr_no = '-'

            dob_str = obj.batuk_dob.strftime('%d-%m-%Y') if obj.batuk_dob else ''
            submitted_str = obj.submitted_at.strftime('%d-%m-%Y %H:%M') if obj.submitted_at else ''

            row_data = [
                sr_no,
                obj.batuk_name,
                dob_str,
                obj.father_name,
                obj.mother_name,
                obj.sub_caste,
                obj.gotra,
                obj.village_city,
                obj.phone_number,
                obj.whatsapp_number,
                obj.home_address,
                obj.attending_members,
                obj.extra_member_notes or '',
                submitted_str,
            ]
            ws.append(row_data)

            for col_idx in range(1, len(row_data) + 1):
                cell = ws.cell(row=row_idx, column=col_idx)
                cell.border = thin_border
                if col_idx in (1, 3, 9, 10, 12, 14):
                    cell.alignment = Alignment(horizontal='center', vertical='center')
                else:
                    cell.alignment = Alignment(horizontal='left', vertical='center')

            row_idx += 1

        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = max(max_len + 5, 14)

        ws.row_dimensions[1].height = 28

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response['Content-Disposition'] = 'attachment; filename=Samuh_Janoi_Registrations.xlsx'
        wb.save(response)
        return response

