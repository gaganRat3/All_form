from django.db import models

class ReferralProgram(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    name = models.CharField(max_length=100, verbose_name="Your Name (Person filling this Form)")
    city = models.CharField(max_length=100, verbose_name="Your City")
    candidate_name = models.CharField(max_length=100, verbose_name="Your Candidate Name (Son/Daughter)")
    candidate_gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name="Candidate Gender")
    candidate_dob = models.DateField(verbose_name="Candidate Date of Birth")
    mobile_no = models.CharField(max_length=15, verbose_name="Your Mobile No.")
    whatsapp_no = models.CharField(max_length=15, verbose_name="Your WhatsApp No.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.candidate_name})"