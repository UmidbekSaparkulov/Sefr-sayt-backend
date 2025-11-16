from django.db import models

class TestInfo(models.Model):
    questions = models.IntegerField()
    minutes = models.IntegerField()
    task_types = models.IntegerField()

    def __str__(self):
        return f"TestInfo ({self.questions} Qs, {self.minutes} min)"

class TestTip(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Expectation(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class SampleQuestion(models.Model):
    task_title = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    prompt = models.TextField()
    preparation = models.CharField(max_length=50)
    speaking = models.CharField(max_length=50)

    def __str__(self):
        return self.task_title

class SampleQuestionGuideline(models.Model):
    sample_question = models.ForeignKey(SampleQuestion, on_delete=models.CASCADE, related_name='guidelines')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
