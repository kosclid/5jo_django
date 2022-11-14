from django.contrib import admin
from .models import Movie, Ost, Movie_rec, Ost_nomal, Comment

# Register your models here.
admin.site.register(Movie)
admin.site.register(Ost)
admin.site.register(Movie_rec)
admin.site.register(Ost_nomal)
admin.site.register(Comment)
