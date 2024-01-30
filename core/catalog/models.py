from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse

# Create your models here.



class Product(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=250)
    category = models.ForeignKey('catalog.Category', verbose_name='Категория', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})


class Category(MPTTModel):
    name = models.CharField('Категория', max_length=150)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name
    