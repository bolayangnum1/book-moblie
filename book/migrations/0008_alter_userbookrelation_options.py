# Generated by Django 4.0.6 on 2022-07-19 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_userbookrelation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userbookrelation',
            options={'verbose_name': 'книга пользователя', 'verbose_name_plural': 'книги пользователей'},
        ),
    ]
