# Generated by Django 3.2.16 on 2022-11-27 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0004_house_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['-active', 'name'], 'verbose_name': 'house', 'verbose_name_plural': 'houses'},
        ),
    ]