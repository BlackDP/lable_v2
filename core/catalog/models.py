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
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'
    
    class MPTTMeta:
        order_insertion_by = ['name']
        
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})
    
    
class PriceType(models.Model):
    name = models.CharField('Вид цены', max_length=50)
    

    class Meta:
        verbose_name = 'Вид цены'
        verbose_name_plural = 'Виды цен'

    def __str__(self):
        return self.name



class ProductPrice(models.Model):
    price_type = models.ForeignKey('catalog.PriceType', verbose_name='Вид цены', on_delete=models.CASCADE)
    price_value = models.DecimalField('Цена', max_digits=8, decimal_places=2)
    product = models.ForeignKey('catalog.Product', verbose_name='Товар', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        unique_together = ['price_type', 'product']

    def __str__(self):
        return f'{self.product} | {self.price_type}: {self.price_value} р.'

    def get_absolute_url(self):
        return reverse('product_price_detail', kwargs={"pk": self.pk})


class Property(models.Model):
    name = models.CharField('Название характеристики', max_length=50)
    # uuid = 
    value_str = models.CharField('Строковое значение', max_length=50, null=True, blank=True)
    # value_list = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return self.name


    
class PropertyValueList(models.Model):
    # uuid = 
    property_id = models.ForeignKey('catalog.Property', verbose_name='Характеристика', on_delete=models.CASCADE)
    value = models.CharField('Значение', max_length=50)
    

    class Meta:
        verbose_name = 'Значение характеристики'
        verbose_name_plural = 'Значения характеристик'

    def __str__(self):
        return f'{self.property_id.name} {self.value}'

    def get_absolute_url(self):
        return reverse("PropertyValueList_detail", kwargs={"pk": self.pk})



class ProductProperty(models.Model):
    product = models.ForeignKey('catalog.Product', verbose_name='Товар', on_delete=models.CASCADE)
    product_property = models.ForeignKey('catalog.Property', verbose_name='Характеристика', on_delete=models.CASCADE)
    public = models.BooleanField(verbose_name='Публичная')
    filtering = models.BooleanField(verbose_name='Фильтр')
    

    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товаров'

    def __str__(self):
        return f'{self.product} {self.product_property}'

    def get_absolute_url(self):
        return reverse("ProductProperty_detail", kwargs={"pk": self.pk})



# Property 
# uuid 
# name 


# Value
# uuid 
# value 
# p_uuid  
# type 