import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_prj.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from scipy.spatial import distance
from recommand.models import Movie, Ost, Ost_nomal

ost_sel = Ost.objects.get(id=1)
print(ost_sel.ost_name)
print(ost_sel.movie_id_id)
ost_sel_num = Ost_nomal.objects.get(ost_id_id=ost_sel.id)
print(ost_sel_num.cluster)


dist_list = []
select_ost_list = [
    ost_sel_num.num_valence,
    ost_sel_num.num_acousticness,
    ost_sel_num.num_danceability,
    ost_sel_num.num_energy,
    ost_sel_num.num_loudness,
    ost_sel_num.num_tempo,
    ost_sel_num.num_gern,
    ost_sel_num.num_mvdir,
]

ost_same_cluster = Ost_nomal.objects.filter(cluster=ost_sel_num.cluster)
for ost_one in ost_same_cluster:
    # print(ost_one.ost_id)

    one_list = [
        ost_one.num_valence,
        ost_one.num_acousticness,
        ost_one.num_danceability,
        ost_one.num_energy,
        ost_one.num_loudness,
        ost_one.num_tempo,
        ost_one.num_gern,
        ost_one.num_mvdir,
    ]
    dist = distance.euclidean(select_ost_list, one_list)
    dist_list.append((ost_one.ost_id_id, dist))
dist_list = sorted(dist_list, key=lambda x: x[1])

recommand_mov_id = []
for sort_dist in dist_list:
    # print(sort_dist[0])

    ost_sort = Ost.objects.get(id=sort_dist[0])
    print(ost_sort.ost_name, ost_sort.movie_id_id)
    if ost_sort.movie_id_id != ost_sel.movie_id_id:
        recommand_mov_id.append(ost_sort.movie_id_id)
    if len(recommand_mov_id) >= 10:
        break
print(recommand_mov_id)

test = Movie.objects.get(movie_id=recommand_mov_id[0])
print(test.movie_name)
