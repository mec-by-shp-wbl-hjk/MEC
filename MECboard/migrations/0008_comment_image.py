# Generated by Django 2.2.3 on 2019-07-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MECboard', '0007_auto_20190722_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to=''),
        ),
    ]