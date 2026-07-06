from datetime import datetime

from django.db import models


class MarriageDoneGiftSubmission(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    filler_name = models.CharField(max_length=100)
    relation = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    candidate_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    candidate_dob = models.DateField()
    spouse_name = models.CharField(max_length=100)
    spouse_dob = models.DateField()
    wedding_photo = models.ImageField(upload_to='marriage_done_photos/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate_name} ({self.filler_name})"

    class Meta:
        verbose_name = 'Marriage Done Gift Submission'
        verbose_name_plural = 'Marriage Done Gift Submissions'
        ordering = ['-submitted_at']
