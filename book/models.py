from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    name = models.CharField(max_length=100, verbose_name='Имя')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    author_name = models.CharField(max_length=255, verbose_name='Автор')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользователь', null=True, related_name='my_book')
    readers = models.ManyToManyField(User, through='UserBookRelation', related_name='books')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=None, null=True)

    def __str__(self):
        return f'name :{self.name}  price :{self.price}'


class UserBookRelation(models.Model):
    class Meta:
        verbose_name = 'книга пользователя'
        verbose_name_plural = 'книги пользователей'

    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f': пользователь: {self.user}  книга: {self.book.name}, рейтинг: {self.rate}'
