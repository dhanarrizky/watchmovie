from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=255)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='documents')
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("hAdmin")
    