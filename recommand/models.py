from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    movie_name = models.CharField(max_length=200)
    year = models.IntegerField()
    movie_dir = models.CharField(max_length=100)
    movie_act = models.CharField(max_length=200)
    movie_ger = models.CharField(max_length=200)
    movie_text = models.TextField(null=True)
    movie_poster = models.ImageField(null=True)

    def __str__(self):
        return f'[{self.movie_id}] : {self.movie_name}({self.year})'


class Ost(models.Model):
    movie_id = models.ForeignKey('Movie', related_name='post', on_delete=models.CASCADE, db_column='movie_id')
    ost_name = models.CharField(max_length=200)
    valence = models.FloatField(null=True, blank=True)
    acousticness = models.FloatField(null=True, blank=True)
    danceability = models.FloatField(null=True, blank=True)
    energy = models.FloatField(null=True, blank=True)
    loudness = models.FloatField(null=True, blank=True)
    tempo = models.FloatField(null=True, blank=True)
    cluster = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.movie_id} : {self.ost_name}'
