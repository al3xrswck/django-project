from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *

def login_view(request):
    pagetitle = "Login"
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('medlager:index'))
    return render(request, 'medlager/login.html', {'login_form': login_form, 'pagetitle': pagetitle})

@login_required
def index(request):
    pagetitle = "Home"
    return render(request, 'medlager/home.html', {'pagetitle': pagetitle})

@login_required
def profile_view(request):
    pagetitle = "Profil"
    usergroups = list(request.user.groups.values_list('name',flat = True))
    return render(request, 'medlager/profile.html', {'pagetitle': pagetitle, 'usergroups': usergroups})

@login_required
def list_vehicle_view(request):
    pagetitle = "Fahrzeuge"
    vehicles = Entity.filter(Type='')
    return render(request, 'medlager/list_vehicle.html', {'pagetitle': pagetitle})

@login_required
def logout_view(request):
    if(request.user.is_authenticated):
        logout(request)
    return redirect(reverse('medlager:login'))