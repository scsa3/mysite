# Generated by Django 2.2 on 2019-04-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_av', '0012_auto_20190425_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actress',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
