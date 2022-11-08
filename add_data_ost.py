# # Ost 데이터 저장
import csv
import os
import django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_prj.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from recommand.models import Movie, Ost

ost = Ost()
ost_list = []

with open('데이터완성본_id추가.csv', encoding='utf8') as csv_file_sub_categories:
    rows = csv.reader(csv_file_sub_categories)
    next(rows, None)
    for row in rows:
        movie = Movie.objects.get(movie_id=row[0])
        movie_id = movie
        ost_name = row[2]

        valence = row[8]
        acousticness = row[8]
        danceability = row[9]
        energy = row[10]
        loudness = row[11]
        tempo = row[12]
        cluster = None

        ost = Ost(movie_id=movie_id, ost_name=ost_name, valence=valence, acousticness=acousticness,
                  danceability=danceability, energy=energy, loudness=loudness, tempo=tempo, cluster=cluster)
        ost_list.append(ost)
        print(ost_name)
print(len(ost_list))
Ost.objects.bulk_create(ost_list)
Ost.objects.all().count()


# # 데이터 수정
# import os
# import django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_prj.settings")
# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# django.setup()
# from recommand.models import Movie, Ost
#
# item = Movie.objects.get(movie_id=0)
# print(item.movie_name)
# item.name = 'My Shop'
# item.save()

# # 데이터 삭제
# import os
# import django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_prj.settings")
# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# django.setup()
# from recommand.models import Movie, Ost
#
# item = Ost.objects.all()
# item.delete()
