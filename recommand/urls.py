from django.urls import path
from recommand import views


urlpatterns = [
    path("", views.home),
    path("search/", views.search, name="search"),
    path("list/<int:sel_id>", views.relist),
    path("list/<int:ost_id>/comments/new/", views.comment_new),
    path("list/<int:ost_id>/comments/<int:com_id>/edit/", views.comment_edit),
    path("list/<int:ost_id>/comments/<int:com_id>/delete/", views.comment_delete),
    path("thank", views.thank, name="thank"),
]
