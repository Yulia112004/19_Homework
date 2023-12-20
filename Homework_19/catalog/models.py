from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    disc = models.CharField(max_length=200, verbose_name='описание')

    def __str__(self):
        return  f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_disc = models.CharField(max_length=200, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за штуку')
    data_created = models.DateField(verbose_name='дата создания')
    data_changed = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.product_name} - {self.price} ({self.category})'

    def short_desription(self):
        return self.product_disc[:100]

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Contact(models.Model):
    country = models.CharField(max_length=100)
    inn = models.CharField(max_length=12)
    adress = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.country} ({self.adress})"



