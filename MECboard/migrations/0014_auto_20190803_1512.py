# Generated by Django 2.2.3 on 2019-08-03 06:12

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MECboard', '0013_board_image_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default='media/default.jpeg', upload_to='media/thumbnail'),
        ),
    ]
