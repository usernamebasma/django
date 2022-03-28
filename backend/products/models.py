from datetime import datetime
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
       return self.name



# Create your models here.
class Product(models.Model):
    image=models.ImageField(null=False,blank=False) 
    name=models.CharField(max_length=200 ,null=False,blank=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=True,null=False) 
    price=models.DecimalField(max_digits=5,decimal_places=2)
    description=models.TextField()
    is_published=models.BooleanField(default=True)
    created_at=models.DateTimeField(default=datetime.now,blank=True)

def __str__(self):
       return self.name

        # class Meta:
        #verbose_name_plural='Order'

