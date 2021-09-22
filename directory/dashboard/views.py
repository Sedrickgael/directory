from django.shortcuts import render , redirect 
from teacher import models
from django.contrib.auth import authenticate, login as login_request, logout
import json
from django.http import JsonResponse
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# default page (all teacher)
def index(request):
    teachers = models.Teacher.objects.filter(statut=True)
    datas = {
        'teachers':teachers,
    }
    return render(request, 'pages/teacher.html', datas)

#  user login 
def login(request):
    datas = {

    }
    return render(request, 'pages/login.html', datas)


# show all subjects
def subjects(request):
    subjects = models.Subject.objects.filter(statut=True)
    datas = {
        'subjects':subjects,
    }
    return render(request, 'pages/subjects.html', datas)

#  teacher profil view
@login_required(login_url = 'login')
def profil(request):
    datas = {

    }
    return render(request, 'pages/profil.html', datas)

# add teacher 
@login_required(login_url = 'login')
def add_teacher(request):
    subjects = models.Subject.objects.filter(statut=True)

    datas = {
        'subjects':subjects,
    }
    return render(request, 'pages/add-teacher.html', datas)


# edit teacher 
@login_required(login_url = 'login')
def edit_teacher(request, slug):
    subjects = models.Subject.objects.filter(statut=True)
    teacher = models.Teacher.objects.get(slug=slug)
    datas = {
        'subjects':subjects,
        'teacher':teacher,
    }
    return render(request, 'pages/add-teacher.html', datas)

# add subject 
@login_required(login_url = 'login')
def add_subject(request):
    datas = {
        
    }
    return render(request, 'pages/add-subjects.html', datas)


# page for edit subect
@login_required(login_url = 'login')
def edit_subject(request, slug):
    try: 
        subject = models.Subject.objects.get(slug=slug)
    except Exception as e:
        print(e)
        return redirect('subjects')
    datas = {
        'subject':subject,
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

@csrf_exempt
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


@csrf_exempt
def post_subject(request):

    postdata = json.loads(request.body.decode('utf-8'))
        
    # name = postdata['name']

    subject_name = postdata['subject_name']
    description = postdata['description']


    # for update
    subject_id = postdata['id']
    message = ""
    success = False
    try:
        try:
            # update
            subject = models.Subject.objects.get(id=int(subject_id))
            message = "Subject updated"
        except:
            # create
            subject = models.Subject()
            message = "Subject created"
        subject.subject_name = subject_name
        subject.description = description
        subject.save()
        success = True


    except Exception as e:
        print(e)
        success = False
        message = str(e)
    data = {
        'success':success,
        'message':message,
    }
    return JsonResponse(data, safe=False)


@csrf_exempt
def delete_subject(request):

    postdata = json.loads(request.body.decode('utf-8'))

    # for delete
    subject_id = postdata['id']
    message = ""
    success = False
    try:
        try:
            # update
            subject = models.Subject.objects.get(id=int(subject_id))
            subject.delete()
            success = True
        except Exception as e:
            print(e)
            message = "error"
    except Exception as e:
        print(e)
        success = False
        message = str(e)
    data = {
        'success':success,
        'message':message,
    }
    return JsonResponse(data, safe=False)


