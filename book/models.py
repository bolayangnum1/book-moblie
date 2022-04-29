from ckeditor_uploader.fields import RichTextUploadingField
from .choicemodels import BOOK_TYPE
from datetime import datetime
from django.core.validators import MaxValueValidator
from django.db import models
from .choicemodels import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name_category = models.CharField('Категория', max_length=100)
    img = models.ImageField('Картинка')

    def __str__(self):
        return f'{self.name_category}'


class BookList(models.Model):

    class Meta:
        verbose_name = 'Список книг'
        verbose_name_plural = 'Список книг'

    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, related_name='category_detail')

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    name = models.CharField('Автор', max_length=100)
    img = models.ImageField('Фото')
    date = models.DateField('Дата рождения')
    date_dead = models.DateField('Дата смерти')

    def __str__(self):
        return f'{self.name}'


class VideoBook(models.Model):

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = "Видео"

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Владелец')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор', related_name='author_video_detail')
    name = models.CharField('Название книги', max_length=100)
    video = models.URLField('Видео')
    rating = models.PositiveSmallIntegerField(verbose_name='рейтинг', validators=[MaxValueValidator(5)])
    book_type = models.CharField(choices=BOOK_TYPE, verbose_name='Тип книги', max_length=100)
    booklist = models.ForeignKey(BookList, on_delete=models.CASCADE, verbose_name='Список книг', related_name='book_video_detail')

    def __str__(self):
        return f'{self.name}'


class ReadBook(models.Model):

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Владелец')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор', related_name='author_read_detail')
    name = models.CharField('Название книги', max_length=100)
    img = models.ImageField('Картинка', upload_to='media/')
    text = models.TextField('О книге')
    copyright_holder = models.CharField('правообладатель', max_length=100)
    book = RichTextUploadingField('Книга')
    rating = models.PositiveSmallIntegerField(verbose_name=('рейтинг'), validators=[MaxValueValidator(5)])
    language = models.CharField('Язык', max_length=50)
    year_book = models.DateField("Дата выхода")
    age_view = models.CharField('рекомендуется к просмотру', max_length=3)
    book_type = models.CharField(choices=BOOK_TYPE, verbose_name='Тип книги', max_length=100)
    book_list = models.ForeignKey(BookList, on_delete=models.CASCADE, verbose_name='Список книг', related_name='read_book_detail')

    def __str__(self):
        return f'{self.name}'


class AudioBook(models.Model):

    class Meta:
        verbose_name = 'Аудио'
        verbose_name_plural = 'Аудио'

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор', related_name='author_audio_detail')
    name = models.CharField('Название книги', max_length=100)
    reader = models.CharField('Чтец', max_length=100)
    img = models.ImageField('Картинка')
    text = models.TextField('О книге')
    copyright_holder = models.CharField('правообладатель', max_length=100)
    audio = models.URLField('Аудио версия')
    rating = models.PositiveSmallIntegerField(verbose_name=('рейтинг'), validators=[MaxValueValidator(5)])
    language = models.CharField('Язык', max_length=50)
    year_book = models.CharField('Год выпуска книги', max_length=4)
    age_view = models.CharField('рекомендуется к просмотру', max_length=3)
    book_type = models.CharField(choices=BOOK_TYPE, verbose_name='Тип книги', max_length=100)
    book_list = models.ForeignKey(BookList, on_delete=models.CASCADE, verbose_name='Список книг', related_name='book_list_detail')

    def __str__(self):
        return f'{self.name}'


class BaseAbstractBook(models.Model):

    class Meta:
        abstract = True

    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='пользователь')
    review = models.CharField(max_length=255, verbose_name='Отзыв')
    created_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата отзыва')
    rating = models.PositiveSmallIntegerField(verbose_name=('рейтинг'), validators=[MaxValueValidator(5)])
    like = models.BooleanField(default=False, verbose_name='Лайк', blank=True, null=True)


class ReviewBook(BaseAbstractBook):
    read_book = models.ForeignKey(ReadBook, verbose_name='Книга', on_delete=models.CASCADE, related_name='review_book_detail')

    class Meta:
        verbose_name = 'Отзывыв'
        verbose_name_plural = 'Отзывы'


class ReviewAudio(BaseAbstractBook):
    audio_book = models.ForeignKey(AudioBook, verbose_name='Книга', on_delete=models.CASCADE, related_name='review_audio_detail')

    class Meta:
        verbose_name = 'Отзывыв'
        verbose_name_plural = 'Отзывы'


class ReviewVideo(BaseAbstractBook):
    video_book = models.ForeignKey(VideoBook, verbose_name='Книга', on_delete=models.CASCADE, related_name='review_video_detail')

    class Meta:
        verbose_name = 'Отзывыв'
        verbose_name_plural = 'Отзывы'
