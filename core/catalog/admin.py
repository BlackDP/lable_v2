from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
from .models import Product, Category, ProductPrice, PriceType


admin.site.register(Product)
admin.site.register(ProductPrice)
admin.site.register(PriceType)
admin.site.register(Category, MPTTModelAdmin)