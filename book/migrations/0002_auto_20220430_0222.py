# Generated by Django 3.2.10 on 2022-04-29 20:22

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название книги')),
                ('img', models.ImageField(upload_to='media/', verbose_name='Картинка')),
                ('text', models.TextField(verbose_name='О книге')),
                ('copyright_holder', models.CharField(max_length=100, verbose_name='правообладатель')),
                ('book', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Книга')),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='рейтинг')),
                ('language', models.CharField(max_length=50, verbose_name='Язык')),
                ('year_book', models.DateField(verbose_name='Дата выхода')),
                ('age_view', models.PositiveSmallIntegerField(max_length=3, verbose_name='рекомендуется к просмотру')),
                ('book_type', models.CharField(choices=[('1', 'Бесплатно'), ('2', 'Премиум')], max_length=100, verbose_name='Тип книги')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.RemoveField(
            model_name='photouser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='readinggoal',
            name='user',
        ),
        migrations.RemoveField(
            model_name='audiobook',
            name='booklist',
        ),
        migrations.RemoveField(
            model_name='booklist',
            name='author',
        ),
        migrations.RemoveField(
            model_name='booklist',
            name='book_type',
        ),
        migrations.RemoveField(
            model_name='booklist',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='book',
        ),
        migrations.AddField(
            model_name='audiobook',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Владелец'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videobook',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.author', verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videobook',
            name='book_type',
            field=models.CharField(choices=[('1', 'Бесплатно'), ('2', 'Премиум')], default=1, max_length=100, verbose_name='Тип книги'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='videobook',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='videobook',
            name='rating',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)], verbose_name='рейтинг'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='audiobook',
            name='author',
        ),
        migrations.AddField(
            model_name='audiobook',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.author', verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='videobook',
            name='booklist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.booklist', verbose_name='Список книг'),
        ),
        migrations.AlterField(
            model_name='videobook',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название книги'),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='PhotoUser',
        ),
        migrations.DeleteModel(
            name='ReadingGoal',
        ),
        migrations.AddField(
            model_name='readbook',
            name='book_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.booklist', verbose_name='Список книг'),
        ),
        migrations.AddField(
            model_name='readbook',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='readbook',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
