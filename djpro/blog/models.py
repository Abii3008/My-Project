from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True,null=True)
    audio = models.FileField(upload_to='audio/',blank=True,null=True)
    video = models.FileField(upload_to='videos/',blank=True,null=True)


  
    def __str__(self):
        return self.title
  