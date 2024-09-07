from django.db import models

class Inquire(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    subject = models.TextField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} - {self.subject}"
