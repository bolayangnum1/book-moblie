from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        # ordering = ('-name',)

    name = models.CharField(max_length=100, verbose_name='Имя')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    author_name = models.CharField(max_length=255, verbose_name='Автор')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользователь', null=True)

    def __str__(self):
        return f'name :{self.name}  price :{self.price}'
