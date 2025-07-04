from django.db import models
from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    images = models.ImageField(upload_to='news/')
    link = models.URLField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


