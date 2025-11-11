from django.db import models

class Writing(models.Model):
    part = models.CharField(max_length=50)
    topic = models.CharField(max_length=100)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.part} - {self.topic}"

