from django.db import models

class GlobalKarmkandDirectoryEntry(models.Model):
    @property
    def brahmanActivities(self):
        return self.brahman_activities

    @property
    def terms(self):
        return self.terms_agreed
    name = models.CharField(max_length=255)
    dob = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    # Experience & Skills
    # Service Preferences
    # File uploads
    brahman_activities = models.CharField(max_length=255)  # Comma-separated values
    experience_years = models.PositiveIntegerField()
    other_skills = models.TextField(blank=True, null=True)
    service_level = models.CharField(max_length=255)  # Comma-separated values
    employment_status = models.CharField(max_length=255)  # Comma-separated values
    photo = models.ImageField(upload_to='karmkand_photos/')
    visiting_card = models.FileField(upload_to='karmkand_visiting_cards/', blank=True, null=True)
    terms_agreed = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.location})"


class KarmkandiMaharajDetails(models.Model):
    maharaj_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    laghurudra_experience = models.PositiveIntegerField()
    residence_city = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Karmkandi Maharaj Details'
        verbose_name_plural = 'Karmkandi Maharaj Details'

    def __str__(self):
        return f"{self.maharaj_name} ({self.residence_city})"


class LaghuRudraYajmanRegistration(models.Model):
    registered_by = models.CharField(max_length=255)
    registered_mobile = models.CharField(max_length=15)
    husband_name = models.CharField(max_length=255)
    wife_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    full_address = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Laghu Rudra Yajman Registration'
        verbose_name_plural = 'Laghu Rudra Yajman Registrations'

    def __str__(self):
        return f"{self.husband_name} & {self.wife_name} ({self.city})"


class ShivMandirShivalayInfo(models.Model):
    temple_name = models.CharField(max_length=255)
    priest_president_name = models.CharField(max_length=255)
    priest_president_phone = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    form_filled_by = models.CharField(max_length=255)
    form_filler_phone = models.CharField(max_length=15)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Shiv Mandir / Shivalay Info'
        verbose_name_plural = 'Shiv Mandir / Shivalay Info'

    def __str__(self):
        return f"{self.temple_name} ({self.city})"
