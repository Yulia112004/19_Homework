from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    disc = models.CharField(max_length=200, verbose_name='описание')
    created_at = models.IntegerField()

    def __str__(self):
        return  f'{self.name} ({self.disc})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    product_disc = models.CharField(max_length=200, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за штуку')
    data_created = models.DateTimeField(verbose_name='дата создания')
    data_changed = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'



