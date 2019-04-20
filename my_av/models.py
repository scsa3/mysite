from django.db import models


class Actress(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Video(models.Model):
    fanart_url = models.URLField(null=True, blank=True)
    poster_url = models.URLField(null=True, blank=True)
    dvd_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    actress = models.ManyToManyField(Actress, null=True, blank=True)
    genre = models.ManyToManyField(Genre, null=True, blank=True)

    def __str__(self):
        return self.dvd_id
