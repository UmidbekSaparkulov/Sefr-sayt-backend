from django.db import models

class Writing(models.Model):
    TYPE_CHOICES = [
        ("letter", "Letter"),
        ("essay", "Essay"),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    themes = models.JSONField()  # array saqlash uchun

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.type})"
