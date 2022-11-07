import pandas as pd
from recommand.models import Movie
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_prj.settings")
# django.setup()


import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_prj.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

django.setup()


df = pd.read_csv('데이터완성본_id추가.csv', encoding='utf8')

for i in range(len(df['movie_name'])):
    Movie.objects.create(
        movie_id=int(df['id'][i]),
        movie_name=df['movie_name'][i],
        year=int(df['year'][i]),
        movie_dir=df['mvdir'][i],
        movie_act=df['mvact'][i],
        movie_ger=df['gerne'][i],
        movie_text='',
        movie_poster=''
    )
    print(df['movie_name'][i])

