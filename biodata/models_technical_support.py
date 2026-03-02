from django.db import models
from django.utils import timezone

class TechnicalSupportRequest(models.Model):
    CATEGORY_CHOICES = [
        ('login_issue', 'Login Issue'),
        ('photo_update', 'Photo Update'),
        ('bio_data_posting', 'Bio Data Posting'),
        ('other', 'Other'),
    ]
    
    
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    
    # Issue Details
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    
        # Metadata
        # status field removed
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.category}"
    
    class Meta:
        verbose_name = "Technical Support Request"
        verbose_name_plural = "Technical Support Requests"
        ordering = ['-created_at']

class SupportAttachment(models.Model):
    support_request = models.ForeignKey(TechnicalSupportRequest, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='support_attachments/')
    filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.support_request} - {self.filename}"
