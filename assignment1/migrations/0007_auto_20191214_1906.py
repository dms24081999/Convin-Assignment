# Generated by Django 3.0 on 2019-12-14 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment1', '0006_auto_20191214_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='blog_url',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
