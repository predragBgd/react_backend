from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    tehnology = models.CharField(max_length=200)