# Generated by Django 2.2 on 2019-05-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_av', '0016_auto_20190515_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file_path',
            field=models.FilePathField(unique=True),
        ),
    ]