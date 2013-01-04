from django.db import models


class Genre(models.Model):
    """The genre of movies or tvshows"""
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class MediaFile(models.Model):
    """The base class for all Movies, Episodes, etc"""
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, null=True, blank=True)
    image = models.URLField(max_length=1000, null=True, blank=True)
    related_mediafiles = models.ManyToManyField('self', symmetrical=True)
    genre = models.ManyToManyField(Genre)

    def __unicode__(self):
        return self.title


class Movie(MediaFile):
    """The basic Movie class"""
    url = models.URLField(max_length=1000, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    imdb = models.FloatField(null=True, blank=True)


class SourceWebsite(models.Model):
    """Website that is used for searching for a given movie or tvshow"""
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, null=True, blank=True)
    image = models.URLField(max_length=1000, null=True, blank=True)
    url_homepage = models.URLField(max_length=1000)
    url_search = models.URLField(
        max_length=2000,
        help_text='Use (*) as a placeholder for the search string.'
    )
    # The search parameter placeholder is "(*)"

    rating = models.FloatField(default=1)

    def __unicode__(self):
        return self.name
