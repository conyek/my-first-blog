# Generated by Django 2.1.1 on 2018-10-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181002_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='background',
            field=models.TextField(default='background'),
        ),
        migrations.AddField(
            model_name='post',
            name='cover_img',
            field=models.ImageField(blank='true', default='null', upload_to='blog/cover'),
        ),
    ]