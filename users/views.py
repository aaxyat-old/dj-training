from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate ,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def profile(request):
    profile = Profile.objects.all()
    context = {"profiles":profile}
    return render(request, "users/profiles.html", context=context)


def user_profile(request,pk):
    user = Profile.objects.get(id=pk)
    context = {"profile":user}
    return render(request, "users/user_profile.html",context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username Not Found")
            
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            messages.error(request, "Username Or Password Incorrect")
    return render(request,"users/login_register.html")


def logoutUser(request):
    logout(request)
    messages.success(request, "User Was Logged Out")
    return redirect("login")