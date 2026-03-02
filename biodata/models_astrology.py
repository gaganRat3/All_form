from django.db import models

class AstrologyFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    candidateName = models.CharField(max_length=100)
    candidateDOB = models.CharField(max_length=100)
    candidateBirthTime = models.CharField(max_length=100)
    candidateBirthPlace = models.CharField(max_length=100)
    description = models.TextField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.candidateName}"
