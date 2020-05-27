from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    country = models.CharField(max_length = 200)
    degree = models.CharField(max_length = 200)
    startdate = models.DateField()
    enddate = models.DateField()
    field = models.CharField(max_length = 200)
    gpa = models.CharField(max_length = 4)