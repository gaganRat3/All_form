from django.db import models

class BookletCampAdvBooking(models.Model):
    name = models.CharField(max_length=100)
    booking_date = models.DateField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100, blank=True, null=True)
    book = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.booking_date})"
