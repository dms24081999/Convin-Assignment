# Generated by Django 3.0 on 2019-12-14 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment1', '0003_registermodel_blog_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registermodel',
            old_name='blog_url',
            new_name='url',
        ),
    ]
