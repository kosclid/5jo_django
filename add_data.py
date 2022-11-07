# import pandas as pd
# from recommand.models import Movie
# import os
# # import django
# # from django.core.wsgi import get_wsgi_application
# # application = get_wsgi_application()
#
# BASE_DIR = os.path.dirname(os.path.abspath())
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_prj.settings")
# # django.setup()
#
# df = pd.read_csv('데이터완성본_1차.csv', encoding='utf8')
#
# for i in range(len(df['movie_name'])):
#     Movie.objects.create(
#         movie_id=int(df['id'][i]),
#         movie_name=df['movie_name'][i],
#         year=int(df['year'][i]),
#         movie_dir=df['mvdir'][i],
#         movie_act=df['mvact'][i],
#         movie_ger=df['gerne'][i],
#         movie_text='',
#         movie_poster=''
#     )
#     print(df['movie_name'][i])


# import csv
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_prj.settings")
# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# django.setup()
# from recommand.models import Movie
#
# movie = Movie()
# with open('데이터완성본_id추가_중복제거.csv', encoding='utf8') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         Movie.objects.create(
#             movie_id=row[0],
#             movie_name=row[1],
#             year=int(row[4]),
#             movie_dir=row[5],
#             movie_act=row[6],
#             movie_ger=row[7],
#             movie_text='',
#             movie_poster=''
#         )
#         print(row)


# # Movie 데이터 저장
# import csv
# import os
# import django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_prj.settings")
# os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# django.setup()
# from recommand.models import Movie, Ost
# movie = Movie()
# movie_list = []
#
# with open('데이터완성본_id추가_중복제거.csv', encoding='utf8') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         movie_id = int(row[0])
#         movie_name = row[1]
#         year = int(row[4])
#         movie_dir = row[5]
#         movie_act = row[6]
#         movie_ger = row[7]
#         movie_text = ''
#         movie_poster = ''
#         movie = Movie(movie_id=movie_id, movie_name=movie_name, year=year, movie_dir=movie_dir, movie_act=movie_act,
#                       movie_ger=movie_ger, movie_text=movie_text, movie_poster=movie_poster)
#         movie_list.append(movie)
#         print(movie_id)
# print(len(movie_list))
# Movie.objects.bulk_create(movie_list)
# Movie.objects.all().count()


# Ost 데이터 저장
import csv
import os
import django

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

        if valence == 'emt':
            valence = None
            acousticness = None
            danceability = None
            energy = None
            loudness = None
            tempo = None

        ost = Ost(movie_id=movie_id, ost_name=ost_name, valence=valence, acousticness=acousticness,
                  danceability=danceability, energy=energy, loudness=loudness, tempo=tempo, cluster=cluster)
        ost_list.append(ost)
        print(ost_name)
print(len(ost_list))
Ost.objects.bulk_create(ost_list)
Ost.objects.all().count()

# 데이터 수정
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
