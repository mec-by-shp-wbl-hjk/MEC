# Generated by Django 2.2.3 on 2019-07-20 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MECboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.NullBooleanField(default=None),
        ),
    ]
