# Generated by Django 3.2.10 on 2022-04-11 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20220411_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data.book')),
            ],
            options={
                'verbose_name': 'Электронная версия книги',
                'verbose_name_plural': 'Электронная версия книги',
            },
        ),
        migrations.DeleteModel(
            name='ChoiceBookMedia',
        ),
    ]