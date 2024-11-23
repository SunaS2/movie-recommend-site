from django.db import models
from movies.models import Movie
from django.conf import settings


# Create your models here.
class Voca(models.Model):
    word = models.TextField()
    word_mean = models.TextField()
    examples = models.TextField(null=True, blank=True)
    memo = models.TextField(null=True, blank=True)
    is_memorized = models.BooleanField(default=False)
    was_memorized = models.BooleanField(default=False)


class VocaNote(models.Model):
    is_public = models.BooleanField(default=True)
    movies = models.ManyToManyField(Movie, related_name="voca_notes")
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="voca_notes")
    vocas = models.ManyToManyField(Voca, related_name="voca_notes")
