from django.db import models

# Create your models here.

class GuruAccount(models.Model):
    uid = models.CharField(max_length=256)
    handle = models.CharField(max_length=256, blank=False)
    score = models.CharField(max_length=256)


class Ticker(models.Model):
    name = models.CharField(max_length=256, blank=False)
    score = models.CharField(max_length=256)
    
    
