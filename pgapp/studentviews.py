from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *

# def studentview(request):
#     context = {"students" : StudentModel.objects.all()}
#     return render(request,"pgapp/homepage.html",context)

def studentdelete(request,id):
    StudentModel.objects.get(id = id).delete()
    return redirect(request.META['HTTP_REFERER'])

def addstudentview(request):
    context = {"rooms" : RoomModel.objects.all(),"preferences" : PreferenceModel.objects.all()}
    return render(request,"pgapp/addstudent.html",context)

def addstudent(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    date_of_birth = request.POST['date_of_birth']
    phone_no = request.POST['phone_no']
    email = request.POST['email']
    blood_group = request.POST['blood_group']
    join_date = request.POST['join_date']
    availed_till = request.POST['availed_till']
    room_id = request.POST['room_id']
    preference_id = request.POST['preference_id']
    room = RoomModel.objects.get(id = room_id)
    preference = PreferenceModel.objects.get(id = preference_id)
    StudentModel(first_name = first_name,
    last_name = last_name,
    date_of_birth = date_of_birth,
    phone_no = phone_no,email = email,
    blood_group = blood_group,
    join_date = join_date,availed_till = availed_till,
    room = room,
    preference = preference
    ).save()


    
    return redirect('homepage')

def studenteditview(request,id):
    student = StudentModel.objects.get(id = id)
    rooms = RoomModel.objects.all()
    preferences = PreferenceModel.objects.all()
    return render(request,"pgapp/studentedit.html",
    {
        'student' : student,
        'rooms' : rooms,
        'preferences' : preferences 
    })

def studentedit(request,id):

    student = StudentModel.objects.get(id = id)
    student.first_name = request.POST['first_name']
    student.last_name = request.POST['last_name']
    student.date_of_birth = request.POST['date_of_birth']
    student.phone_no = request.POST['phone_no']
    student.email = request.POST['email']
    student.blood_group = request.POST['blood_group']
    student.join_date = request.POST['join_date']
    student.availed_till = request.POST['availed_till']

    student.room = RoomModel.objects.get(id = request.POST['room_id'])
    student.preference = PreferenceModel.objects.get(id = request.POST['preference_id'])
    student.save()

    return redirect('homepage')