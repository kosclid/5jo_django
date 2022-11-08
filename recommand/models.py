from django.db import models
from accounts.models import User
from django.core.validators import MaxValueValidator


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    movie_name = models.CharField(max_length=200)
    year = models.IntegerField()
    movie_dir = models.CharField(max_length=100)
    movie_act = models.CharField(max_length=200)
    movie_ger = models.CharField(max_length=200)
    movie_text = models.TextField(null=True, blank=True)
    movie_poster = models.ImageField(upload_to='recommand/images/poster')
    rader_chart = models.ImageField(upload_to='recommand/images/rader')

    def __str__(self):
        return f'[{self.movie_id}] : {self.movie_name}({self.year})'


class Ost(models.Model):
    movie_id = models.ForeignKey('Movie', on_delete=models.CASCADE, db_column='movie_id')
    ost_name = models.CharField(max_length=200)
    valence = models.FloatField()
    acousticness = models.FloatField()
    danceability = models.FloatField()
    energy = models.FloatField()
    loudness = models.FloatField()
    tempo = models.FloatField()
    cluster = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.movie_id} : {self.ost_name}'


class Movie_recommand(models.Model):
    ost_id = models.ForeignKey('Ost', on_delete=models.CASCADE, db_column='ost_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    recodation = models.CharField(max_length=200)


class User_rating(models.Model):
    recommand_id = models.ForeignKey('Movie_recommand', on_delete=models.CASCADE, db_column='recommand_id')
    review = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2),], null=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, db_column='movie_id')
