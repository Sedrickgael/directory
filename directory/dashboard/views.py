from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    datas = {

    }
    return render(request, 'pages/teacher.html', datas)


def login(request):
    datas = {

    }
    return render(request, 'pages/login.html', datas)



def subjects(request):
    datas = {

    }
    return render(request, 'pages/subjects.html', datas)



def profil(request):
    datas = {

    }
    return render(request, 'pages/profil.html', datas)



def add_subject(request):
    datas = {

    }
    return render(request, 'pages/add-subjects.html', datas)

