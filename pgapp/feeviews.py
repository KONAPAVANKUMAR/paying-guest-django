from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *

def addfee(request,studentid):
    amount = request.POST['amount']
    date = request.POST['date']
    status = request.POST['status']
    fee = FeesModel(amount = amount,date = date,status = status)
    fee.save()

    student = StudentModel.objects.get(id = studentid)
    student.fees.add(fee)
    return redirect(request.META['HTTP_REFERER'])

def deletefee(request,feeid):
    FeesModel.objects.get(id = feeid).delete()
    return redirect(request.META['HTTP_REFERER'])

def addmessfee(request,studentid):
    amount = request.POST['amount']
    date = request.POST['date']
    status = request.POST['status']
    messfee = MessFeesModel(amount = amount,date = date,status = status)
    messfee.save()

    student = StudentModel.objects.get(id = studentid)
    student.mess_fees.add(messfee)
    return redirect(request.META['HTTP_REFERER'])

def deletemessfee(request,messfeeid):
    MessFeesModel.objects.get(id = messfeeid).delete()
    return redirect(request.META['HTTP_REFERER'])