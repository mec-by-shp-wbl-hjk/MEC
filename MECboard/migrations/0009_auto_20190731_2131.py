# Generated by Django 2.2.3 on 2019-07-31 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MECboard', '0008_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to='media/images'),
        ),
    ]
