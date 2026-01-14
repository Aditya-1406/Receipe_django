from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Receipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    receipe_name = models.CharField(max_length= 100)
    receipe_description = models.TextField()
    image = models.ImageField(upload_to='vegpic/')
    category = models.ForeignKey(Category,on_delete=models.PROTECT)

    def __str__(self):
        return self.receipe_name


