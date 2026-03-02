from django.db import models

class BusinessDirectoryEntry(models.Model):
    BUSINESS_TYPE_CHOICES = [
        ('Online Business', 'Online Business'),
        ('Offline Business', 'Offline Business'),
        ('Online + Offline Business', 'Online + Offline Business'),
    ]

    ownerName = models.CharField(max_length=200)
    businessName = models.CharField(max_length=200)
    businessType = models.CharField(max_length=30, choices=BUSINESS_TYPE_CHOICES)
    services = models.TextField(blank=True)
    businessSegment = models.CharField(max_length=100, blank=True)
    service_locations = models.CharField("Which City / State / Country You provide Your Business Services", max_length=200, blank=True)
    address = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='business_directory/', blank=True, null=True)
    ownerPhoto = models.ImageField(upload_to='business_directory/owner_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.businessName} ({self.ownerName})"
