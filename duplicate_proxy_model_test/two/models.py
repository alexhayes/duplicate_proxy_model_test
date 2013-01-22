from django.db import models

class Two(models.Model):
    name = models.CharField(max_length=16)