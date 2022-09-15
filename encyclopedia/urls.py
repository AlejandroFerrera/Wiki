from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("not-found/", views.not_found, name="not_found"),
    path("wiki/<str:title>", views.page, name="page"),
    path("search/", views.search, name="search"),
    path("new-page", views.new_page, name="new-page")

]   
