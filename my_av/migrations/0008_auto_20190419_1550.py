# Generated by Django 2.2 on 2019-04-19 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_av', '0007_auto_20190419_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='actress',
            field=models.ManyToManyField(blank=True, null=True, to='my_av.Actress'),
        ),
        migrations.AlterField(
            model_name='video',
            name='genre',
            field=models.ManyToManyField(blank=True, null=True, to='my_av.Genre'),
        ),
    ]
