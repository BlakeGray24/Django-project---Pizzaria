# Generated by Django 3.0.5 on 2022-12-12 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0012_auto_20221211_2245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'comments'},
        ),
    ]