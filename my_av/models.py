from django.db import models


class Actress(models.Model):
    name = models.CharField(max_length=200, blank=True)
    art_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    sample_url = models.URLField(null=True, blank=True)
    plot = models.CharField(max_length=3000, null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    fanart_url = models.URLField(null=True, blank=True)
    poster_url = models.URLField(null=True, blank=True)
    dvd_id = models.CharField(max_length=200)
    release_date = models.DateField(null=True, blank=True)

    # TODO: Foreign key for these
    # director =
    # set =
    # studio =
    actress = models.ManyToManyField(Actress, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    file_path = models.CharField(max_length=500)

    def __str__(self):
        return self.dvd_id
