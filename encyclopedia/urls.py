from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("not-found/<str:title>", views.not_found, name="not_found"),
    path("wiki/<str:title>", views.page, name="page"),
    path("search/", views.search, name="search"),
    path("new-page/", views.new_page, name="new-page"),
    path("edit-page/<str:title>", views.edit_page, name="edit-page"),
    path("random-page", views.random_page, name="random-page")
]   
