from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=5, unique=True)  # A1, B1, C1
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)  # Reading, Listening, Speaking, Writing
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

