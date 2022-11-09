import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_prj.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from recommand.models import Movie, Ost
mo_id = [0, 1, 2]

ost_all = []

for mov_id in mo_id:
    forign = Ost.objects.filter(movie_id_id=mov_id)
    ost_one = []
    for ost_num in forign:
        ost_one.append(ost_num.ost_name)
    ost_all.append(ost_one)

print(ost_all)