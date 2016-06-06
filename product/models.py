from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Products(models.Model):
    #author = models.ForeignKey('auth.User')
    pname=models.CharField(max_length=100,default="")
    photo=models.ImageField(upload_to='photo')
    description=models.CharField(max_length=200,default="")

    def __str__(self):
        return self.pname
