from django.db import models

class Speaking(models.Model):
    part = models.CharField(max_length=50)
    topic = models.CharField(max_length=100)
    question = models.TextField()
    audio_file = models.FileField(upload_to='speaking/audio/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return f"{self.part} - {self.topic}"
