from django.db import models


class Submission(models.Model):
    """
    Stores each form submission.
    profile_image is saved to /media/profile_images/
    created_at is set automatically when the record is created.
    """
    name          = models.CharField(max_length=150)
    email         = models.EmailField()
    city          = models.CharField(max_length=100)
    message       = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/')
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'

    def __str__(self):
        return f"{self.name} — {self.email}"
