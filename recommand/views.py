from django.shortcuts import render
from recommand.models import Movie


# Create your views here.

def index(request):
    poster = Movie.objects.all().order_by('movie_id')
    return render(
        request,
        "recommand/index.html",
        {'poster': poster, })
