from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *

def staffview(request):
    context = {"staffs" : StaffModel.objects.all()}
    return render(request,"pgapp/staff.html",context)

def staffdelete(request,id):
    StaffModel.objects.get(id = id).delete()
    return redirect(request.META['HTTP_REFERER'])

def staffeditview(request,id):
    staff = StaffModel.objects.get(id = id)
    return render(request,"pgapp/staffedit.html",{'staff' : staff})

def staffedit(request,id):
    name = request.POST['name']
    salary = request.POST['salary']
    staff = StaffModel.objects.get(id = id)
    staff.name = name
    staff.salary = salary
    staff.save()
    return redirect('staffpage')

def addstaffview(request):
    return render(request,"pgapp/addstaff.html")



def addstaff(request):
    name = request.POST['name']
    salary = request.POST['salary']
    StaffModel(name = name,salary = salary).save()
    return redirect('staffpage')