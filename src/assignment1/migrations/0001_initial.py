# Generated by Django 3.0 on 2019-12-14 21:52

import assignment1.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('blog_url', models.URLField(blank=True, max_length=500)),
                ('photo', models.FileField(upload_to='event/photo/', validators=[assignment1.validators.validate_photo_extension])),
                ('cv', models.FileField(blank=True, upload_to='event/cv/', validators=[assignment1.validators.validate_cv_extension])),
            ],
        ),
    ]
