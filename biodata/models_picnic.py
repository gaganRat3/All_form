from django.db import models

class PicnicRegistration(models.Model):
    filler_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email_address = models.EmailField(default='', blank=True)
    city = models.CharField(max_length=100)
    candidate_name = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    RELATION_CHOICES = [
        ('Self', 'Self'),
        ('Son', 'Son'),
        ('Daughter', 'Daughter'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister'),
        ('Other', 'Other'),
    ]
    relation = models.CharField(max_length=10, choices=RELATION_CHOICES)
    dob = models.DateField()
    persons = models.PositiveIntegerField()
    is_coming = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate_name} ({self.filler_name})"
