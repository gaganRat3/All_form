from django.test import TestCase

from .models_karmkand_directory import ShivMandirShivalayInfo


class ShivMandirShivalayInfoModelTests(TestCase):
    def test_create_record(self):
        record = ShivMandirShivalayInfo.objects.create(
            temple_name='Shiv Temple',
            priest_president_name='Pandit Ji',
            priest_president_phone='9876543210',
            city='Ahmedabad',
            form_filled_by='Rakesh',
            form_filler_phone='9123456780',
        )

        self.assertEqual(record.temple_name, 'Shiv Temple')
        self.assertEqual(record.city, 'Ahmedabad')
        self.assertTrue(record.pk)
