# Generated by Django 2.2.3 on 2019-08-02 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MECboard', '0011_auto_20190802_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='image',
        ),
    ]
