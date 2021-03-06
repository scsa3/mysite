# Generated by Django 2.2 on 2019-04-17 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_av', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActressTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VideoTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dvd_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ActressLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_av.ActressTest')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_av.VideoTest')),
            ],
        ),
    ]
