from django.contrib import admin
from .models import Movie, Ost, Movie_recommand, User_rating
# Register your models here.
admin.site.register(Movie)
admin.site.register(Ost)
admin.site.register(Movie_recommand)
admin.site.register(User_rating)