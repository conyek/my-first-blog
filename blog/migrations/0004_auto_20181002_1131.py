# Generated by Django 2.1.1 on 2018-10-02 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181002_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='subtitle here', max_length=400),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='title here', max_length=200),
        ),
    ]
