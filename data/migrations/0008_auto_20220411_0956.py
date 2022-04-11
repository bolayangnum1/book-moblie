# Generated by Django 3.2.10 on 2022-04-11 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20220411_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicebook',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data.book', verbose_name='Книга'),
        ),
        migrations.CreateModel(
            name='ChoiceAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data.audio', verbose_name='Книга')),
            ],
            options={
                'verbose_name': 'Электронная версия книги',
                'verbose_name_plural': 'Электронная версия книги',
            },
        ),
    ]
