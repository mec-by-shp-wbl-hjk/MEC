# Generated by Django 2.2.3 on 2019-08-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MECboard', '0009_auto_20190731_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='media/images'),
        ),
    ]
