from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^profile/', views.profile),
    url(r'^create_playlist/', views.create_playlist),
]
