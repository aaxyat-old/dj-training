from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .models import *
from .forms import CustomUserCreationForm, ProfileForm

# Create your views here.

def profile(request):
    profile = Profile.objects.all()
    context = {"profiles": profile}
    return render(request, "users/profiles.html", context=context)


def user_profile(request, pk):
    user = Profile.objects.get(id=pk)
    context = {"profile": user}
    return render(request, "users/user_profile.html", context)


@login_required(login_url="login")
def user_account(request):
    profile = request.user.profile
    context = {"profile": profile}
    return render(request,"users/account.html", context=context)


@login_required(login_url="login")
def edit_account(request):

    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":

        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():

            data = form.save(commit=False)
            if not data.name :
                data.name = "John Doe"
            data.email = profile.email
            data.save()
            return redirect("account")
        else:
            return redirect("edit-profile")


    context = {'form':form}
    return render(request, "users/profile_form.html", context=context)



def loginPage(request):
    page = 'login'
    context = {'page':page}
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username Not Found")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            messages.error(request, "Username Or Password Incorrect")
    return render(request, "users/login_register.html", context=context)


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,"User Created Successfully")
            login(request, user)
            return redirect("edit-account")
        else:
            messages.error(request,"User creation Error")
            #return redirect("register")

            


    context = {"page":page, "form":form}
    return render(request,"users/login_register.html", context=context)


def logoutUser(request):
    logout(request)
    messages.success(request, "User Was Logged Out")
    return redirect("login")
