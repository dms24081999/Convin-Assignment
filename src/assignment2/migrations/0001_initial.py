# Generated by Django 3.0 on 2019-12-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('document_hash', models.CharField(max_length=255)),
                ('document', models.FileField(blank=True, upload_to='documents/')),
            ],
        ),
    ]
