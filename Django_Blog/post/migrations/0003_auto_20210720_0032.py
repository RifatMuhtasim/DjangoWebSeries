# Generated by Django 3.2.5 on 2021-07-19 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210719_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startpost',
            old_name='StartPostBody',
            new_name='Body',
        ),
        migrations.RenameField(
            model_name='startpost',
            old_name='StartPostBodyImage',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='startpost',
            old_name='StartPostTitle',
            new_name='Title',
        ),
    ]
