from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
from .models import Product, Category


admin.site.register(Product)
admin.site.register(Category, MPTTModelAdmin)