# Generated by Django 3.2.6 on 2021-08-19 20:05

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='loadimg')),
                ('title', models.CharField(max_length=200)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('meta', ckeditor.fields.RichTextField()),
                ('body', ckeditor.fields.RichTextField()),
                ('url', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
