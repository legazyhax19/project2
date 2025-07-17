
from django.urls import path
from Jameapp import views
from django.contrib import admin

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('tree/', views.tree, name='tree'),
    path('person/', views.person, name='person')
]
