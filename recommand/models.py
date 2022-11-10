from django.db import models
from accounts.models import User
from django.core.validators import MaxValueValidator
from scipy.spatial import distance


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

    def __str__(self):
        return f'{self.movie_id} : {self.ost_name}'


class Ost_nomal(models.Model):
    ost_id = models.ForeignKey('Ost', on_delete=models.CASCADE, db_column='ost_id')
    num_valence = models.FloatField()
    num_acousticness = models.FloatField()
    num_danceability = models.FloatField()
    num_energy = models.FloatField()
    num_loudness = models.FloatField()
    num_tempo = models.FloatField()
    num_gern = models.IntegerField()
    num_mvdir = models.IntegerField()
    cluster = models.IntegerField()


class Movie_recommand(models.Model):
    ost_id = models.ForeignKey('Ost', on_delete=models.CASCADE, db_column='ost_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    recodation = models.CharField(max_length=200)


class User_rating(models.Model):
    recommand_id = models.ForeignKey('Movie_recommand', on_delete=models.CASCADE, db_column='recommand_id')
    review = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2), ], null=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, db_column='movie_id')


def ost_search(movie_all):
    mo_id = movie_all
    ost_all = []
    for mov_id in mo_id:
        forign = Ost.objects.filter(movie_id_id=mov_id)
        ost_one = []
        for ost_num in forign:
            ost_one.append(ost_num.ost_name)
        ost_all.append(ost_one)
    return (ost_all)

def movie_recomand(ch_ost):
    ost_sel = Ost.objects.get(id=ch_ost)
    # print(ost_sel.ost_name)
    # print(ost_sel.movie_id_id)
    ost_sel_num = Ost_nomal.objects.get(ost_id_id=ost_sel.id)
    # print(ost_sel_num.cluster)
    dist_list = []
    select_ost_list = [ost_sel_num.num_valence, ost_sel_num.num_acousticness, ost_sel_num.num_danceability,
                       ost_sel_num.num_energy,
                       ost_sel_num.num_loudness, ost_sel_num.num_tempo, ost_sel_num.num_gern, ost_sel_num.num_mvdir]

    ost_same_cluster = Ost_nomal.objects.filter(cluster=ost_sel_num.cluster)
    for ost_one in ost_same_cluster:
        # print(ost_one.ost_id)

        one_list = [ost_one.num_valence, ost_one.num_acousticness, ost_one.num_danceability, ost_one.num_energy,
                    ost_one.num_loudness, ost_one.num_tempo, ost_one.num_gern, ost_one.num_mvdir]
        dist = distance.euclidean(select_ost_list, one_list)
        dist_list.append((ost_one.ost_id_id, dist))
    dist_list = sorted(dist_list, key=lambda x: x[1])

    recommand_mov_id = []
    for sort_dist in dist_list:
        # print(sort_dist[0])

        ost_sort = Ost.objects.get(id=sort_dist[0])
        # print(ost_sort.ost_name, ost_sort.movie_id_id)
        if ost_sort.movie_id_id != ost_sel.movie_id_id:
            recommand_mov_id.append(ost_sort.movie_id_id)
        if len(recommand_mov_id) >= 10:
            break
    return recommand_mov_id
    # print(recommand_mov_id)