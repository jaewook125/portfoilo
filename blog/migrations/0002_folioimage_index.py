# Generated by Django 2.0.4 on 2018-04-27 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folioimage',
            name='index',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.Index'),
            preserve_default=False,
        ),
    ]