# Generated by Django 2.2.3 on 2019-07-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MECboard', '0004_auto_20190722_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='down',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='filename',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='filesize',
            field=models.IntegerField(default=0),
        ),
    ]
