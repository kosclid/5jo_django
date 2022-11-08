from django.shortcuts import render
from recommand.models import Movie, Ost


# Create your views here.

def index(request):
    poster = Movie.objects.all().order_by('movie_id')
    return render(
        request,
        "recommand/index.html",
        {'poster': poster, })


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # recipes = Movie.objects.filter(movie_name__icontains=searched)
        recipes = Movie.objects.get(movie_name=searched)
        movie = Movie.objects.get(movie_name=searched)
        a = movie.movie_id
        forign = Ost.objects.filter(movie_id_id=a)
        return render(request, 'recommand/searched.html', {'searched': searched, 'recipes': recipes, 'forign': forign})
    else:
        return render(request, 'recommand/searched.html', {})
