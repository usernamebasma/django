from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from .models import Product 
class ProductForm(forms.ModelForm):
   class Meta:
       model = Product
       fields=['image','name','category','price','description']
       widgets= {
           'image': forms.FileInput(attrs={'class':'form_control'}),
           'name': forms.TextInput(attrs={'class':'form_control'}),
           'category': forms.Select(attrs={'class':'form_control'}),
           'price': forms.TextInput(attrs={'class':'form_control'}),
           'description': forms.TextInput(attrs={'class':'form_control'})
       }

      