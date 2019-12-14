# Generated by Django 2.2.7 on 2019-12-14 11:41

import assignment1.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='cv',
            field=models.FileField(blank=True, upload_to='event/cv/', validators=[assignment1.validators.validate_cv_extension]),
        ),
        migrations.AlterField(
            model_name='registermodel',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='registermodel',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='registermodel',
            name='photo',
            field=models.FileField(blank=True, upload_to='event/photo/', validators=[assignment1.validators.validate_photo_extension]),
        ),
    ]
