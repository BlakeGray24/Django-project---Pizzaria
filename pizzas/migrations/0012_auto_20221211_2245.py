# Generated by Django 3.0.5 on 2022-12-12 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0011_auto_20221211_2122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'posts'},
        ),
    ]
