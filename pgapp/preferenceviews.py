from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *

def preferenceview(request):
    context = {"preferences" : PreferenceModel.objects.all()}
    return render(request,"pgapp/preference.html",context)

def preferencedelete(request,id):
    PreferenceModel.objects.get(id = id).delete()
    return redirect(request.META['HTTP_REFERER'])

def addpreferenceview(request):
    return render(request,"pgapp/addpreference.html")

def addpreference(request):
    description = request.POST['description']
    extra_charges = request.POST['extra_charges']
    PreferenceModel(description = description,extra_charges = extra_charges).save()
    return redirect('preferencepage')