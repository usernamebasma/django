#from venv import create
from pyexpat import model
from django.contrib import admin
from .models import Product
from .models import Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
   list_display=('id','name','category','price','is_published','created_at')
   list_display_link=('id','name')
   list_Filter=('price',)
   list_editable=('is_published',)
   search_fields=('name','price')
   ordering=('price',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Category)