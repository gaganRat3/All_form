from django.db import models


class DiwaliGiftCard(models.Model):
    candidate_name = models.CharField(max_length=150, verbose_name="Candidate Name")
    website_name = models.CharField(max_length=150, verbose_name="Website Name")
    membership_id = models.CharField(max_length=100, verbose_name="Membership ID")
    whatsapp_number = models.CharField(max_length=20, verbose_name="WhatsApp Number")
    home_address = models.TextField(verbose_name="Home Address")
    mobile_number = models.CharField(max_length=20, verbose_name="Mobile Number")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="Submitted At")

    class Meta:
        verbose_name = "Diwali Gift Card"
        verbose_name_plural = "Diwali Gift Cards"
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.candidate_name} - {self.membership_id} ({self.website_name})"

