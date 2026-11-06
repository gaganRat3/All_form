import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biodata_project.settings')
django.setup()

from django.test import Client, RequestFactory
from django.urls import reverse
from django.contrib.admin.sites import site
from biodata.models_samuh_janoi import SamuhJanoiRegistration
from biodata.admin_samuh_janoi import SamuhJanoiRegistrationAdmin
import io
import openpyxl

def run_tests():
    print("=== STARTING SAMUH JANOI AUTOMATED TESTS ===")
    client = Client()

    # 1. Test GET form
    print("\n1. Testing GET on /samuh-janoi/...")
    url = reverse('samuh_janoi_form')
    response = client.get(url)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    html = response.content.decode('utf-8')
    assert "સમૂહ જનોઈ રજીસ્ટ્રેશન ફોર્મ" in html, "Page title missing in HTML"
    assert "batuk_name" in html, "batuk_name field missing"
    assert "batuk_dob" in html, "batuk_dob field missing"
    assert "father_name" in html, "father_name field missing"
    assert "mother_name" in html, "mother_name field missing"
    assert "sub_caste" in html, "sub_caste field missing"
    assert "gotra" in html, "gotra field missing"
    assert "home_address" in html, "home_address field missing"
    assert "village_city" in html, "village_city field missing"
    assert "phone_number" in html, "phone_number field missing"
    assert "whatsapp_number" in html, "whatsapp_number field missing"
    assert "attending_members" in html, "attending_members field missing"
    assert "31-12-2021" in html, "Policy note missing in HTML"
    print("-> GET /samuh-janoi/ passed successfully!")

    # 2. Test aliases
    print("\n2. Testing alias URLs...")
    res_alias = client.get('/Samuh_Janoi/')
    assert res_alias.status_code == 200, f"Expected 200 on /Samuh_Janoi/, got {res_alias.status_code}"
    print("-> Alias /Samuh_Janoi/ works!")

    # 3. Test Invalid POST (empty)
    print("\n3. Testing Empty POST (validation errors)...")
    res_empty = client.post(url, {})
    assert res_empty.status_code == 200, "Empty POST should return form with errors"
    empty_content = res_empty.content.decode('utf-8')
    assert "કૃપા કરીને નીચે મુજબની ભૂલો સુધારો" in empty_content, "Error alert missing from rendered page"
    assert "બટુકનું પૂરું નામ" in empty_content, "Batuk name error missing"
    assert "ફોન નંબર" in empty_content, "Phone number error missing"
    print("-> Empty submission validation passed!")

    # 4. Test Invalid Phone & Date
    print("\n4. Testing Invalid Phone & Invalid Member count...")
    res_bad = client.post(url, {
        'batuk_name': 'આર્યન શર્મા',
        'batuk_dob': '2015-05-10',
        'mother_name': 'ગીતાબેન શર્મા',
        'father_name': 'રાજેશભાઈ શર્મા',
        'sub_caste': 'ઓદિચ્ય સહસ્ર બ્રાહ્મણ',
        'gotra': 'કશ્યપ',
        'home_address': '૧૦૧, શિવમ રેસિડેન્સી, સેટેલાઇટ, અમદાવાદ - ૩૮૦૦૧૫',
        'village_city': 'અમદાવાદ',
        'phone_number': '123', # bad
        'whatsapp_number': '9876543210',
        'attending_members': '-5', # bad
    })
    assert res_bad.status_code == 200
    bad_content = res_bad.content.decode('utf-8')
    assert "માન્ય ૧૦ આંકડાનો ફોન નંબર" in bad_content
    assert "સભ્યોની સંખ્યા 0 અથવા તેથી વધુ" in bad_content
    print("-> Invalid phone & invalid members validation passed!")

    # 5. Test Successful POST
    print("\n5. Testing Valid POST (Submission)...")
    initial_count = SamuhJanoiRegistration.objects.count()
    valid_data = {
        'batuk_name': 'બટુક શૌર્ય દેવરાજભાઈ ત્રિવેદી',
        'batuk_dob': '15-08-2016',
        'mother_name': 'ભાવનાબેન ત્રિવેદી',
        'father_name': 'દેવરાજભાઈ હરીશભાઈ ત્રિવેદી',
        'sub_caste': 'ઔદીચ્ય સહસ્ર બ્રાહ્મણ',
        'gotra': 'ભારદ્વાજ',
        'home_address': 'A-402, શ્રીજી ટાવર, ગુરુકુળ રોડ, મેમનગર, અમદાવાદ - 380052',
        'village_city': 'અમદાવાદ',
        'phone_number': '9825012345',
        'whatsapp_number': '9825012345',
        'attending_members': '15',
        'extra_member_notes': 'અંદાજે ૧૫ થી ૨૦ સભ્યો ઉપસ્થિત રહેશે.',
    }
    res_post = client.post(url, valid_data, follow=True)
    assert res_post.status_code == 200, f"Expected 200 after redirect, got {res_post.status_code}"
    assert SamuhJanoiRegistration.objects.count() == initial_count + 1, "Record was not created in DB!"

    new_record = SamuhJanoiRegistration.objects.latest('submitted_at')
    assert new_record.batuk_name == valid_data['batuk_name']
    assert str(new_record.batuk_dob) == '2016-08-15'
    assert new_record.father_name == valid_data['father_name']
    assert new_record.mother_name == valid_data['mother_name']
    assert new_record.sub_caste == valid_data['sub_caste']
    assert new_record.gotra == valid_data['gotra']
    assert new_record.village_city == valid_data['village_city']
    assert new_record.phone_number == '9825012345'
    assert new_record.whatsapp_number == '9825012345'
    assert new_record.attending_members == 15
    print("-> Record verified in Database!")

    # Check Success Page content
    success_html = res_post.content.decode('utf-8')
    assert "રજીસ્ટ્રેશન સફળતાપૂર્વક નોંધાઈ ગયું છે" in success_html
    assert "બટુક શૌર્ય દેવરાજભાઈ ત્રિવેદી" in success_html
    assert "15-08-2016" in success_html
    assert "દેવરાજભાઈ હરીશભાઈ ત્રિવેદી" in success_html
    assert "31-12-2021" in success_html
    print("-> Success page confirmed rendering all submitted fields!")

    # Test 5b: Zero member count is allowed
    print("\n5b. Testing Attending Members = 0...")
    data_zero = dict(valid_data)
    data_zero['attending_members'] = '0'
    data_zero['batuk_name'] = 'ટેસ્ટ બટુક ઝીરો મેમ્બર'
    res_zero = client.post(url, data_zero, follow=True)
    assert res_zero.status_code == 200
    zero_record = SamuhJanoiRegistration.objects.get(batuk_name='ટેસ્ટ બટુક ઝીરો મેમ્બર')
    assert zero_record.attending_members == 0
    zero_record.delete()
    print("-> 0 attending members accepted and stored successfully!")

    # 6. Test Admin Panel Registration
    print("\n6. Testing Admin Panel Registration & Methods...")
    assert SamuhJanoiRegistration in site._registry, "SamuhJanoiRegistration is NOT registered in admin.site!"
    admin_instance = site._registry[SamuhJanoiRegistration]
    assert isinstance(admin_instance, SamuhJanoiRegistrationAdmin)
    print("-> SamuhJanoiRegistration is properly registered in Django Admin!")

    # 7. Test Admin Excel Export
    print("\n7. Testing Admin Excel Export...")
    from django.contrib.auth.models import User
    admin_user, _ = User.objects.get_or_create(username='test_admin_user', is_staff=True, is_superuser=True)
    rf = RequestFactory()
    req = rf.get('/admin/biodata/samuhjanoiregistration/')
    req.user = admin_user
    admin_instance.get_changelist_instance(req)

    queryset = SamuhJanoiRegistration.objects.filter(pk=new_record.pk)
    excel_response = admin_instance.export_selected_to_excel(req, queryset)
    assert excel_response.status_code == 200
    assert excel_response['Content-Type'] == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    # Check that openpyxl can read the exported workbook
    wb = openpyxl.load_workbook(io.BytesIO(excel_response.content))
    ws = wb.active
    assert ws.title == "Samuh Janoi Registrations"
    # Row 1 is header
    header_values = [cell.value for cell in ws[1]]
    assert "બટુક નું પૂરું નામ" in header_values
    assert "પિતા નું નામ" in header_values
    assert "આવનાર સભ્યો સંખ્યા" in header_values

    # Row 2 is data
    row2_values = [cell.value for cell in ws[2]]
    assert valid_data['batuk_name'] in row2_values
    assert 15 in row2_values
    print("-> Admin Excel export verified successfully!")

    print("\n=== ALL TESTS PASSED SUCCESSFULLY! ===")

if __name__ == '__main__':
    run_tests()
