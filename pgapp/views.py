from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *
# Create your views here.
def homepageview(request):
    if not request.user.is_authenticated:
        return redirect('loginpage')
    context = {'user' : request.user,"students" : StudentModel.objects.all()}
    return render(request,"pgapp/homepage.html",context)


def loginview(request):
    return render(request,"pgapp/login.html")

def signupview(request):
    return render(request,"pgapp/signup.html")

def registeruser(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    print(username,password)
    if password!=password2:
        messages.add_message(request,messages.INFO,"passwords not matched")
        return redirect(request.META['HTTP_REFERER'])




    if User.objects.filter(username = username).exists():
        messages.add_message(request,messages.INFO,"user already exists ! choose a different name")
        return redirect(request.META['HTTP_REFERER'])
    
    User.objects.create_user(username = username,password = password)
    messages.add_message(request,messages.INFO,"user succesfully registered")
    return redirect('loginpage')

def authenticateuser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username,password = password)
    if user is not None:
        login(request,user)
        return redirect('homepage')
    messages.add_message(request, messages.INFO, 'invalid credentials')
    return redirect(request.META["HTTP_REFERER"])

def logoutuser(request):
    logout(request)
    messages.add_message(request,messages.INFO,"you have logged out succesfully")
    return redirect('loginpage')



# student
def studentdetailview(request,id):
    student = StudentModel.objects.get(id = id)
    context = {'student' : student}
    # print(student)
    return render(request,"pgapp/studentdetail.html",context)