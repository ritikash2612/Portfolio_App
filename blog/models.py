from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 150)
    pub_date = models.DateTimeField()
    body = models.CharField(max_length = 300)
    image = models.ImageField(upload_to='images/')