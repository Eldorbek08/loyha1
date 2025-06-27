from django.db import models

# Create your models here.

class Group(models.Model):
    ism = models.CharField(max_length=255)
    familya = models.CharField(max_length=255)
    images = models.ImageField(upload_to='group/')
    tajriba = models.CharField(max_length=255)
    mutaxasislig = models.CharField(max_length=255)
    
    def __str__(self):
        return self.ism