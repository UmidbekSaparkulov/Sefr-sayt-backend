from django.db import models
from core.models import Level, Skill


class ListeningTest(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="listening_tests")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="listening_tests")
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=50)  # multiple-choice, gap-fill, true-false
    audio_file = models.FileField(upload_to="listening/audio/")
    transcript = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=10, default="en")

    def __str__(self):
        return f"{self.title} ({self.level.name})"


class ListeningQuestion(models.Model):
    listening_test = models.ForeignKey(ListeningTest, on_delete=models.CASCADE, related_name="questions")
    order = models.PositiveIntegerField(default=1)
    text = models.TextField(blank=True, null=True)
    question_type = models.CharField(max_length=50, default="multiple-choice")
    correct_answer = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"Q{self.order} - {self.listening_test.title}"


class ListeningOption(models.Model):
    question = models.ForeignKey(ListeningQuestion, on_delete=models.CASCADE, related_name="options")
    key = models.CharField(max_length=5)  # A, B, C, D
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.key} - {self.text[:30]}"
