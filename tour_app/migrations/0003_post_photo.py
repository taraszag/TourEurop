# Generated by Django 3.2.6 on 2021-08-22 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_app', '0002_auto_20210821_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Photo',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
