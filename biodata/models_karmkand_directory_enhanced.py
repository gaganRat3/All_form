from django.db import models
from django.core.validators import FileExtensionValidator

class GlobalKarmkandDirectoryEntry(models.Model):
    """Enhanced model for Global Karmkand Directory registration"""
    
    # Personal Information
    name = models.CharField(max_length=255, verbose_name="Full Name")
    dob = models.CharField(max_length=50, verbose_name="Date of Birth")
    location = models.CharField(max_length=255, verbose_name="Location/City")
    address = models.TextField(verbose_name="Complete Address", blank=True)
    phone1 = models.CharField(max_length=20, verbose_name="Primary Phone")
    phone2 = models.CharField(max_length=20, blank=True, null=True, verbose_name="Secondary Phone")
    email = models.EmailField(blank=True, null=True, verbose_name="Email Address")
    whatsapp = models.CharField(max_length=20, blank=True, null=True, verbose_name="WhatsApp Number")
    
    # Experience & Skills
    brahman_activities = models.CharField(max_length=500, verbose_name="Brahman Activities/Specializations")
    experience_years = models.PositiveIntegerField(verbose_name="Years of Experience")
    other_skills = models.TextField(blank=True, null=True, verbose_name="Other Skills & Qualifications")
    languages_known = models.CharField(max_length=255, blank=True, verbose_name="Languages Known")
    
    # Service Preferences
    service_level = models.CharField(max_length=500, verbose_name="Service Level Preferences")
    employment_status = models.CharField(max_length=500, verbose_name="Employment Status")
    
    # File uploads
    photo = models.ImageField(
        upload_to='karmkand_photos/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        verbose_name="Profile Photo"
    )
    visiting_card = models.FileField(
        upload_to='karmkand_visiting_cards/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],
        verbose_name="Visiting Card"
    )
    
    # Terms and conditions
    terms_agreed = models.BooleanField(default=False, verbose_name="I agree to the terms and conditions")
    
    # Timestamps
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Global Karmkand Directory Entry"
        verbose_name_plural = "Global Karmkand Directory Entries"
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"{self.name} ({self.location})"
    
    def get_puja_types_list(self):
        """Return puja types as a list"""
        return self.service_level.split(',') if self.service_level else []
    
    def get_employment_status_list(self):
        """Return employment status as a list"""
        return self.employment_status.split(',') if self.employment_status else []
    
    def get_brahman_activities_list(self):
        """Return brahman activities as a list"""
        return self.brahman_activities.split(',') if self.brahman_activities else []
