from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Link(models.Model):
    name = models.CharField(max_length=180)
    w1 = models.CharField(max_length=400)
    w2 = models.CharField(max_length=400)
    w3 = models.CharField(max_length=400)
    w4 = models.CharField(max_length=400)
    w5 = models.CharField(max_length=400)

    def __str__(self):
        return self.name 
