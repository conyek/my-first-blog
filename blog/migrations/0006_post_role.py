# Generated by Django 2.1.1 on 2018-10-04 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181004_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='role',
            field=models.TextField(blank='true', default='role'),
        ),
    ]
