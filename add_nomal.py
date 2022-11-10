# Movie 데이터 저장
import csv
import os
import django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_prj.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from recommand.models import Ost, Ost_nomal

ost_nom_list = []
with open('clusterdata.csv', encoding='utf8') as csv_file_sub_categories:
    rows = csv.reader(csv_file_sub_categories)
    next(rows, None)
    for row in rows:
        ost = Ost.objects.get(id=int(row[0])+1)
        ost_id = ost
        cluster = int(row[3])
        num_gern = float(row[4])
        num_mvdir = float(row[5])
        num_valence = float(row[6])
        num_acousticness = float(row[7])
        num_danceability = float(row[8])
        num_energy = float(row[9])
        num_loudness = float(row[10])
        num_tempo = float(row[11])

        ost_nom = Ost_nomal(ost_id=ost_id, cluster=cluster, num_gern=num_gern, num_mvdir=num_mvdir,
                            num_valence=num_valence, num_acousticness=num_acousticness, num_danceability=num_danceability,
                            num_energy=num_energy, num_loudness=num_loudness, num_tempo=num_tempo)
        ost_nom_list.append(ost_nom)
        print(row[1])
print(len(ost_nom_list))
Ost_nomal.objects.bulk_create(ost_nom_list)
Ost_nomal.objects.all().count()


# with open('clusterdata.csv', encoding='utf8') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         item = Ost_nomal.objects.get(ost_id=int(row[0])+1)
#         if item.ost_name == row[2]:
#             item.cluster = row[-1]
#         else:
#             print(row[2])
#         item.save()
#         print('------진행중--------')
# print('done')
