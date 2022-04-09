from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models

from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Author(models.Model):
    name = models.CharField('Автор', max_length=100)
    img = models.ImageField('Фото', upload_to='media/')
    date = models.DateField('Дата рождения')


class Book(models.Model):

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    name = models.CharField('Название книги', max_length=100)
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.PROTECT)
    reader = models.CharField('Чтец', max_length=100)
    img = models.ImageField('Картинка', upload_to='media/')
    text = models.TextField('О книге')
    copyright_holder = models.CharField('правообладатель', max_length=100)
    book = RichTextUploadingField('Книга')
    price = models.DecimalField('Цена', max_digits=12, decimal_places=2)
    language = models.CharField('Язык', max_length=50)
    rating = models.PositiveSmallIntegerField(
        verbose_name=_('рейтинг'),
        validators=[MaxValueValidator(5)]
    )
    tags = TaggableManager()

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='пользователь')
    book = models.OneToOneField(Book, on_delete=models.PROTECT, verbose_name='Книга')
    review = models.CharField(max_length=255, verbose_name='Отзыв')
    created_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата отзыва')
    rating = models.PositiveSmallIntegerField(
        verbose_name=_('рейтинг'),
        validators=[MaxValueValidator(5)]
    )
    tags = TaggableManager()

    def __str__(self):
        return f'{self.book}'

    class Meta:
        verbose_name = 'Отзывыв'
        verbose_name_plural = 'Отзывы'


TIME_PERIOD = (('1', '7 Дней'),
               ('2', '14 Дней'),
               ('3', '30 Дней'),
               ('4', '365 Дней')
               )


class ReadingGoal(models.Model):
    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = "Цели"

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, verbose_name='Я прочитаю')
    time_period = models.CharField(choices=TIME_PERIOD, max_length=50, verbose_name='За период')
