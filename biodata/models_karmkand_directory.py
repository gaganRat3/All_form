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
