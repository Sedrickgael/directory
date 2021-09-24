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
            return JsonResponse(datas,safe=False) 
                
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
            # delete
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


@csrf_exempt
def delete_teacher(request):

    postdata = json.loads(request.body.decode('utf-8'))

    # for delete
    teacher_id = postdata['id']
    message = ""
    success = False
    try:
        try:
            # delete
            teacher = models.Teacher.objects.get(id=int(teacher_id))
            teacher.delete()
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

@csrf_exempt
def post_form(request):
    try:
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")
        subjects_taught = request.POST.get("subjects_taught").rsplit(',')
        print(subjects_taught, "333333333333333333333")
        phone_number = request.POST.get("phone_number")
        room_number = request.POST.get("room_number")
        teacher_id = request.POST.get("id")
        print("################################", subjects_taught)

        # check if teacher have more than 5 subjects
        if len(subjects_taught) > 5:
            success = False
            message = "Teacher can't have more than five(5) subjects"
            
        else:
            try:
                # update
                teacher = models.Teacher.objects.get(id=int(teacher_id))
                message = "Teacher updated"
            except Exception as e:
                # create
                teacher = models.Teacher()
                message = "Teacher created"
            teacher.last_name = last_name
            teacher.first_name = first_name
            teacher.email = email

            teacher.phone_number = phone_number
            teacher.room_number = room_number
            teacher.save()
            teacher.subjects_taught.clear()

            # save picture
            try:
                profile_picture = request.FILES["profile_picture"]
                teacher.profile_picture = profile_picture
                teacher.save()
            except:
                pass

            # save subjectt taught
            for subject in subjects_taught:
                print(subject, "&&&&&&&&&&&&&&&&&&&&&&&")
                teacher.subjects_taught.add(subject.rsplit("|")[1])
            teacher.save()
            success = True

    except Exception as e :
        print(e)
        success = False
        message = "An error occurred"
    data = {
        'success':success,
        'message':message,
    }
    return JsonResponse(data, safe=False)






@csrf_exempt
def upload_file(request):
    error = False
    success =False
    message = ""
    try:
        teachers_csv = request.FILES["teachers_csv"]
        uploaded_file = models.UploadFile()
        uploaded_file.upload_file = teachers_csv
        uploaded_file.save()

        # open file in read
        with open(uploaded_file.upload_file.path, 'r' ) as reader:
            all_teachers_in_file = reader.readlines()

            for i in range(1, len(all_teachers_in_file)):
                if all_teachers_in_file[i].rsplit(',')[3] is not None and all_teachers_in_file[i].rsplit(',')[3] != "" and all_teachers_in_file[i].rsplit(',')[0] is not None and all_teachers_in_file[i].rsplit(',')[0] != "" and all_teachers_in_file[i].rsplit(',')[2] is not None and all_teachers_in_file[i].rsplit(',')[2] != "":
                    
                    try:
                        # check if mail is used
                        teacher = models.Teacher.objects.get(email=all_teachers_in_file[i].rsplit(',')[3])
                        error = True
                    except:
                        # create teacher
                        teacher = models.Teacher()
                        teacher.last_name = all_teachers_in_file[i].rsplit(',')[1]
                        teacher.first_name = all_teachers_in_file[i].rsplit(',')[0]
                        teacher.email = all_teachers_in_file[i].rsplit(',')[3]

                        teacher.phone_number = all_teachers_in_file[i].rsplit(',')[4]
                        teacher.room_number = all_teachers_in_file[i].rsplit(',')[5]
                        teacher.save()

                        # save subject 
                        if '"' in all_teachers_in_file[i]:
                            subjects = all_teachers_in_file[i].rsplit('"')[1]
                        else:
                            subjects = all_teachers_in_file[i].rsplit(',')[6]
                        if ", " in subjects:
                            subjects = subjects.replace(", ", ",")
                        for subject in subjects.rsplit(','):
                            try:
                                subject_e = models.Subject.objects.get(subject_name__icontains=subject)
                            except:
                                subject_e = models.Subject()
                                subject_e.subject_name = subject
                                subject_e.save()
                            # add subject to teacher
                            if teacher.subjects_taught.count() < 5 :
                                teacher.subjects_taught.add(subject_e.id)
                                teacher.save()
                            else:
                                error = True
                        teacher.save()
                        # save profile picture
                        try:
                            profile_picture = "Teachers/" + all_teachers_in_file[i].rsplit(',')[2]
                            teacher.profile_picture = profile_picture
                            teacher.save()
                        except:
                            pass
                    success = True
                    message = "Success"
                else:
                    error = True
    except:
        success = False
        message = "An error occurred"
    if error:
        message = "Datas loaded with error"
    data = {
        'success':success,
        'errorr':error,
        'message':message,
    }
    return JsonResponse(data, safe=False)
