# 데이터 수정
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie_prj.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from recommand.models import Movie
import re

movie = Movie.objects.all()

n=0

for i in range(0, len(movie)):
    item = Movie.objects.get(movie_id=i)
    m_n = item.movie_name
    if 'Borat' in m_n:
        m_n = m_n.split(':')[0].strip()
    print(m_n)
    m_n = re.sub(r'[^\w]', ' ', m_n)
    m_n = m_n.replace("'", "")
    m_n = m_n.replace('  ', ' ')
    year = item.year
    sech = m_n+'_'+str(year)
    image = 'static/img/{}.png'.format(sech)
    item.movie_poster = image
    item.save()
print(n)


