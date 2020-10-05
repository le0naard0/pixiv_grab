from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    author_URL = models.CharField(max_length=200, blank=True, null=True)
    URL = models.TextField()
    name = models.CharField(max_length=100)
    author_load_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)
    NSFW = models.CharField(max_length=1, default='0')

    def load(self):
        self.created_date = timezone.now()
        self.save()
    
    
    def __str__(self):
        return self.author + ' ' + self.name