# Generated by Django 2.2 on 2019-04-18 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_av', '0004_auto_20190418_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='fanart_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]