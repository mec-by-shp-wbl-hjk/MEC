# Generated by Django 2.2.3 on 2019-08-03 06:38

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MECboard', '0014_auto_20190803_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='media/thumbnail'),
        ),
    ]