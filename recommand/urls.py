from django.urls import path
from recommand import views



urlpatterns = [
    path('', views.home),
    path('search/', views.search, name='search'),
    path('list/<int:sel_id>', views.relist),

]


