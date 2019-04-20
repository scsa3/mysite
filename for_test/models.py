from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=250, unique=True)


class Movie(models.Model):
    name = models.CharField(max_length=250)
    genre = models.ManyToManyField(Genre)
