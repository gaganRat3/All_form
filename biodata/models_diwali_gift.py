from django.db import models


class DiwaliGiftRegistration(models.Model):
    candidate_name = models.CharField(max_length=150, verbose_name="Candidate Name")
    dob = models.CharField(max_length=50, verbose_name="Date of Birth")
    current_city = models.CharField(max_length=150, verbose_name="Current City")
    candidate_mobile = models.CharField(max_length=20, verbose_name="Candidate Mobile Number")
    parents_mobile = models.CharField(max_length=20, verbose_name="Parents Mobile Number")

    # Courier Delivery Details
    contact_person = models.CharField(max_length=150, verbose_name="Contact Person")
    address = models.TextField(verbose_name="Full Address")
    contact_mobile = models.CharField(max_length=20, verbose_name="Mobile Number")
    pincode = models.CharField(max_length=10, verbose_name="Area Pincode")

    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted At")

    class Meta:
        verbose_name = "Diwali Gift Registration"
        verbose_name_plural = "Diwali Gift Registrations"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.candidate_name} - {self.current_city} ({self.candidate_mobile})"

