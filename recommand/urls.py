from django.urls import path
from recommand import views

urlpatterns = [
    path('', views.index),

]
