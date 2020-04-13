from django import forms
from django.db import models
from recruitment_app.short_url import shorten_url


#Create model LongURl
class LongURL(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    longurl = models.URLField( blank=True, unique=True)
    owner = models.ForeignKey('auth.User', related_name='longurl', on_delete=models.CASCADE)
    shorturl = models.URLField(blank=True, default=shorten_url)

    class Meta:
        ordering = ['created']