from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("add/", views.add_content, name="add"),
    path("edit/", views.edit_content, name="edit"),
    path("save/", views.save_content, name="save"),
    path("random/", views.random_content, name="random")
]
