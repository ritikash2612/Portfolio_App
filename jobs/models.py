from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    duration_from = models.DateField()
    duration_Till = models.DateField()
    summary = models.TextField()
    responsibility = models.TextField()