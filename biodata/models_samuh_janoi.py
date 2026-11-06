from django.db import models


class SamuhJanoiRegistration(models.Model):
    batuk_name = models.CharField(
        max_length=200,
        verbose_name="બટુક નું પૂરું નામ (Batuk's Full Name)"
    )
    batuk_dob = models.DateField(
        verbose_name="બટુક ની જન્મ-તારીખ (Batuk's Date of Birth)"
    )
    mother_name = models.CharField(
        max_length=200,
        verbose_name="બટુક ની માતા નું પૂરું નામ (Mother's Full Name)"
    )
    father_name = models.CharField(
        max_length=200,
        verbose_name="બટુક ના પિતા નું પૂરું નામ (Father's Full Name)"
    )
    sub_caste = models.CharField(
        max_length=150,
        verbose_name="આપ કેવા બ્રાહ્મણ છો - પેટા-જ્ઞાતિ (Brahmin Sub-Caste)"
    )
    gotra = models.CharField(
        max_length=120,
        verbose_name="આપનું ગૌત્ર શું છે ? (Gotra)"
    )
    home_address = models.TextField(
        verbose_name="આપનું ઘર નું સરનામું પિનકોડ સાથે (Residential Address with Pincode)"
    )
    village_city = models.CharField(
        max_length=150,
        verbose_name="આપનું ગામ / શહેર નું નામ (Village / City)"
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name="ફોન નંબર (Phone Number)"
    )
    whatsapp_number = models.CharField(
        max_length=20,
        verbose_name="વોટ્સેપ નંબર (WhatsApp Number)"
    )
    submitted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="સબમિશન તારીખ / સમય (Submitted At)"
    )

    class Meta:
        verbose_name = "સમૂહ જનોઈ રજીસ્ટ્રેશન (Samuh Janoi Registration)"
        verbose_name_plural = "સમૂહ જનોઈ રજીસ્ટ્રેશન (Samuh Janoi Registrations)"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.batuk_name} - {self.village_city} ({self.phone_number})"

