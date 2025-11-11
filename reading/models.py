from django.db import models
from core.models import Level, Skill


class ReadingTest(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="reading_tests")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="reading_tests")
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=50)  # fill-the-gaps, matching, comprehension, mixed
    language = models.CharField(max_length=10, default='en')
    instructions = models.TextField(blank=True, null=True)
    passage = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.level.name})"


class Option(models.Model):
    reading_test = models.ForeignKey(ReadingTest, on_delete=models.CASCADE, related_name="options")
    key = models.CharField(max_length=5)
    word = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="reading/ads/", blank=True, null=True)

    def __str__(self):
        return f"{self.key} - {self.word or self.text[:30]}"


class Question(models.Model):
    reading_test = models.ForeignKey(ReadingTest, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField(blank=True, null=True)
    question_type = models.CharField(max_length=50, blank=True, null=True)
    order = models.PositiveIntegerField(default=1)
    correct_answer = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"Q{self.order} - {self.reading_test.title}"


class Segment(models.Model):
    reading_test = models.ForeignKey(ReadingTest, on_delete=models.CASCADE, related_name="segments")
    order = models.PositiveIntegerField()
    text_before = models.TextField(blank=True, null=True)
    gap_number = models.PositiveIntegerField(blank=True, null=True)
    text_after = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Segment {self.order} ({self.reading_test.title})"


class Paragraph(models.Model):
    reading_test = models.ForeignKey(ReadingTest, on_delete=models.CASCADE, related_name="paragraphs")
    order = models.PositiveIntegerField()
    text = models.TextField()

    def __str__(self):
        return f"Paragraph {self.order} ({self.reading_test.title})"


class Heading(models.Model):
    reading_test = models.ForeignKey(ReadingTest, on_delete=models.CASCADE, related_name="headings")
    key = models.CharField(max_length=5)
    text = models.TextField()

    def __str__(self):
        return f"Heading {self.key}"

