# Generated by Django 2.2 on 2019-04-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_av', '0008_auto_20190419_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='actress',
            name='art_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]