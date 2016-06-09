from django.db import models

class Products(models.Model):
    user = models.ForeignKey('auth.User')
    pname=models.CharField(max_length=50,default="")
    photo=models.ImageField(upload_to='photo')
    description=models.CharField(max_length=100,default="")

    def __str__(self):
        return self.pname
