# Generated by Django 2.2 on 2019-04-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_av', '0009_actress_art_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='actress',
            field=models.ManyToManyField(blank=True, to='my_av.Actress'),
        ),
        migrations.AlterField(
            model_name='video',
            name='genre',
            field=models.ManyToManyField(blank=True, to='my_av.Genre'),
        ),
    ]
