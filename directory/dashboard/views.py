from django.shortcuts import render , redirect 
from . import models
from django.contrib.auth import authenticate, login as login_request, logout
import json
from django.http import JsonResponse
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

# default page (all teacher)
def index(request):
    datas = {

    }
    return render(request, 'pages/teacher.html', datas)

#  user login 
def login(request):
    datas = {

    }
    return render(request, 'pages/login.html', datas)


# show all subjects
def subjects(request):
    datas = {

    }
    return render(request, 'pages/subjects.html', datas)

#  teacher profil view
@login_required(login_url = 'login')
def profil(request):
    datas = {

    }
    return render(request, 'pages/profil.html', datas)


# page for add subect
@login_required(login_url = 'login')
def add_subject(request):
    datas = {

    }
    return render(request, 'pages/add-subjects.html', datas)

# LOGOUT VIEW
def deconnexion(request):
    logout(request)
    return redirect('login')

#######################################################################
#######################################################################
############################ POST VIEWS ###############################
#######################################################################
#######################################################################


def islogin(request):

    postdata = json.loads(request.body.decode('utf-8'))
        
    # name = postdata['name']

    username = postdata['username']
    password = postdata['password']

    isSuccess = False
    u_type = ''
    try:
        if '@' in username:
            user = authenticate(email=username, password=password)
            utilisateur = User.objects.get(email=username)
            print(username)
        else:
            user = authenticate(username=username, password=password)
            utilisateur = User.objects.get(username=username)
            
        if user is not None and user.is_active:
            print("user is login")
            isSuccess = True
            login_request(request, user)
            datas = {
                'success':True,
                'message':'Vous êtes connectés!!!',
            }
            return JsonResponse(datas,safe=False) # page si connect
                
        else:
            data = {
                'success':False,
                'message':'Vos identifiants ne sont pas correcte',
            }
            return JsonResponse(data, safe=False)
    except Exception as e:
        print(e)
        data = {
            'success':False,
            'message':"Merci de verifier vos informations d'authentification",
        }
        return JsonResponse(data, safe=False)


