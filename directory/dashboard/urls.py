from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subjects', views.subjects, name='subjects'),
    path('profil', views.profil, name='profil'),
    path('add/teacher', views.add_teacher, name='add_teacher'),
    path('add/subject', views.add_subject, name='add_subject'),
    path('edit/subject/<str:slug>', views.edit_subject, name='edit_subject'),
    path('edit/teacher/<str:slug>', views.edit_teacher, name='edit_teacher'),

    ########################################################
    ############## AUTHENTICATION ####################################
    ########################################################
    path('login', views.login, name='login'),
    path('deconnexion', views.deconnexion, name='logout'),

    ########################################################
    ############## POST ####################################
    ########################################################
    path('post_login', views.islogin, name='post_login'),
    path('post_subject', views.post_subject, name='post_subject'),
    path('delete_subject', views.delete_subject, name='delete_subject'),
]
