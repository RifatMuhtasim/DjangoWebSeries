# Generated by Django 3.2.6 on 2021-08-24 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexblog',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
