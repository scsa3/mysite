# Generated by Django 2.2 on 2019-04-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_av', '0002_actresslink_actresstest_videotest'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
