# Generated by Django 2.2 on 2019-04-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_av', '0006_video_poster_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='ActressLink',
        ),
        migrations.DeleteModel(
            name='ActressTest',
        ),
        migrations.DeleteModel(
            name='VideoTest',
        ),
        migrations.AddField(
            model_name='video',
            name='genre',
            field=models.ManyToManyField(to='my_av.Genre'),
        ),
    ]
