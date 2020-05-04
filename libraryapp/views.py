from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    pass

def user_login(request):
    pass

def client_add(request):
    pass

def client_remove(request):
    pass

def client_details(request):
    pass
