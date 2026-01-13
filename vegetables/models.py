from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Receipe(models.Model):

    receipe_name = models.CharField(max_length= 100)
    receipe_description = models.TextField()
    image = models.ImageField(upload_to='vegpic/')
    category = models.ForeignKey(Category,on_delete=models.PROTECT)

    def __str__(self):
        return self.receipe_name


