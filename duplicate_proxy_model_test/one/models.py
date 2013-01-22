from django.db import models

class One(models.Model):
    name = models.CharField(max_length=16)