from django.db import models

from django.db import models
# Create your models here.
# MVC MODEL view controler

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def _unicode_(self):
        return self.title

    def _str_(self):
        return self.title
