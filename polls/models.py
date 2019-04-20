import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Video(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    runtime = models.IntegerField(default=0)
    director = models.CharField(max_length=200)
    studio = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    dvd_id = models.CharField(max_length=200)
    series = models.CharField(max_length=200)
    content_id = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Actress(models.Model):
    name = models.CharField(max_length=200)


class ActressLink(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    actress = models.ForeignKey(Actress, on_delete=models.CASCADE)
    cast_order = models.IntegerField(default=0)
