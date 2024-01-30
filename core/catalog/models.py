from django.db import models
from django.urls import reverse

# Create your models here.



class Product(models.Model):
    name = models.CharField('Наименование', max_length=250)
    

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})


