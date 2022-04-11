# Generated by Django 3.2.10 on 2022-04-10 10:30

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('data', '0004_alter_author_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название книги')),
                ('reader', models.CharField(max_length=100, verbose_name='Чтец')),
                ('img', models.ImageField(upload_to='media/', verbose_name='Картинка')),
                ('text', models.TextField(verbose_name='О книге')),
                ('copyright_holder', models.CharField(max_length=100, verbose_name='правообладатель')),
                ('book', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Книга')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена')),
                ('language', models.CharField(max_length=50, verbose_name='Язык')),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='рейтинг')),
                ('year_book', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Год выпуска книги')),
                ('age_view', models.CharField(max_length=3, verbose_name='рекомендуется к просмотру')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.author', verbose_name='Автор')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='age_view',
            field=models.CharField(default=1, max_length=3, verbose_name='рекомендуется к просмотру'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='year_book',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Год выпуска книги'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ChoiceBookMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='data.audio', verbose_name='Есть Аудиоверсия')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='data.book', verbose_name='Электронная версия')),
            ],
        ),
    ]