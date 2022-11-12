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
    movie_link = models.CharField(max_length=200)

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
    rader_chart = models.ImageField(upload_to='recommand/images/rader')

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


class Movie_rec(models.Model):
    ost_id = models.ForeignKey('Ost', on_delete=models.CASCADE, db_column='ost_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    user_name = models.CharField(max_length=200)
    ch_ost_name = models.CharField(max_length=200)
    ch_mov_name = models.CharField(max_length=200)
    rec_ost_name = models.CharField(max_length=200)
    rec_mov_name = models.CharField(max_length=200)
    review = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user_id} : {self.ch_ost_name}_{self.rec_ost_name}'

    def get_absolute_url(self):
        return f'/recommand/list/{self.ost_id_id}'

def ost_movie(ost_id):
    chs_ost = Ost.objects.get(id=ost_id)
    wt_mv_id = chs_ost.movie_id_id
    return wt_mv_id


def mv_ost_recomand(ch_ost):
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

    recommand_ost_id = []
    recommand_mov_id =[]
    for sort_dist in dist_list:
        # print(sort_dist[0])

        ost_sort = Ost.objects.get(id=sort_dist[0])
        # print(ost_sort.ost_name, ost_sort.movie_id_id)
        if ost_sort.movie_id_id != ost_sel.movie_id_id:
            if ost_sort.movie_id_id not in recommand_mov_id:
                recommand_ost_id.append(ost_sort.id)
                recommand_mov_id.append(ost_sort.movie_id_id)

        if len(recommand_ost_id) >= 10:
            break
    recommand_list = [recommand_mov_id, recommand_ost_id]
    return recommand_list
