# Generated by Django 2.2.3 on 2019-07-22 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MECboard', '0003_auto_20190722_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
