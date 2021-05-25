from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *

def addvisitor(request,studentid):
    student = StudentModel.objects.get(id = studentid)
    visitor = VisitorModel(
        name = request.POST['name'],
        phone_no = request.POST['phone_no'],
        in_time = request.POST['in_time'],
        out_time=request.POST['out_time'])
    visitor.save()
    student.visitor.add(visitor)
    student.save()
    print(student.visitor.all())
    return redirect(request.META['HTTP_REFERER'])

def deletevisitor(request,visitorid):
    VisitorModel.objects.get(id = visitorid).delete()
    return redirect(request.META['HTTP_REFERER'])
    

