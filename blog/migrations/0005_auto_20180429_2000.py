# Generated by Django 2.0.4 on 2018-04-29 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180429_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='category_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='index',
            name='thumbnail_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
