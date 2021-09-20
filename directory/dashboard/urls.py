from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('subjects', views.subjects, name='subjects'),
    path('profil', views.profil, name='profil'),
    path('add_subject', views.add_subject, name='add_subject'),
]
