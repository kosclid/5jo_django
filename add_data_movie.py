# Movie 데이터 저장
import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_prj.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from recommand.models import Movie, Ost
movie = Movie()
movie_list = []

with open('데이터완성본_id추가_중복제거.csv', encoding='utf8') as csv_file_sub_categories:
    rows = csv.reader(csv_file_sub_categories)
    next(rows, None)
    for row in rows:
        movie_id = int(row[0])
        movie_name = row[1]
        year = int(row[4])
        movie_dir = row[5]
        movie_act = row[6]
        movie_ger = row[7]
        movie_text = ''
        movie_poster = ''
        movie = Movie(movie_id=movie_id, movie_name=movie_name, year=year, movie_dir=movie_dir, movie_act=movie_act,
                      movie_ger=movie_ger, movie_text=movie_text, movie_poster=movie_poster)
        movie_list.append(movie)
        print(movie_id)
print(len(movie_list))
Movie.objects.bulk_create(movie_list)
Movie.objects.all().count()