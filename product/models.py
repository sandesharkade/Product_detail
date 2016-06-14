from django.db import models

class Products(models.Model):
    user = models.ForeignKey('auth.User')
    name=models.CharField(max_length=50,default="")
    photo=models.ImageField(upload_to='photo')
    description=models.TextField()

    def __str__(self):
        return self.name
