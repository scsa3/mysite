# Generated by Django 2.2 on 2019-04-18 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_av', '0003_video_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
