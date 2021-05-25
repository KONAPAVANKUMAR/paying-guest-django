from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *

def roomtypeview(request):
    context = {"roomtypes" : RoomTypeModel.objects.all()}
    return render(request,"pgapp/roomtype.html",context)

def roomtypedelete(request,id):
    RoomTypeModel.objects.get(id = id).delete()
    return redirect(request.META['HTTP_REFERER'])

def addroomtypeview(request):
    return render(request,"pgapp/addroomtype.html")

def addroomtype(request):
    description = request.POST['description']
    fees = request.POST['fees']
    RoomTypeModel(description = description,fees = fees).save()
    return redirect('roomtypepage')