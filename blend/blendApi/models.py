from django.db import models

class Render(models.Model):
    inputPath = models.CharField(max_length=200)
    outputPath = models.CharField(max_length=200)
    reqDate = models.DateField()