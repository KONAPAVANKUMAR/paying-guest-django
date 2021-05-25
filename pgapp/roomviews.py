from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *

def roomview(request):
    context = {"rooms" : RoomModel.objects.all()}
    return render(request,"pgapp/room.html",context)

def roomdelete(request,id):
    RoomModel.objects.get(id = id).delete()
    return redirect(request.META['HTTP_REFERER'])

def addroomview(request):
    context = {"staffs" : StaffModel.objects.all(),"roomtypes" : RoomTypeModel.objects.all()}
    return render(request,"pgapp/addroom.html",context)

def addroom(request):
   
    room_no = request.POST['room_no']
    floor = request.POST['floor']
    availablity = request.POST['availablity']
    staffid = request.POST['staffid']
    staff = StaffModel.objects.get(id = staffid)
    room_type_id = request.POST['roomtypeid']
    room_type = RoomTypeModel.objects.get(id = room_type_id)
    
    RoomModel(room_no = room_no,floor = floor,availablity = availablity,staff = staff,room_type = room_type).save()
    return redirect('roompage')