from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser
from django.contrib import messages
from django.db import connection
#from create_acc.models import passenger
import sqlite3

def registration(request):
    form = CreateUser()

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            #user = form.cleaned_data.get('username')
            # messages.success(request,'Account created successfully! Dear '+ user)
            return redirect('login')
    context = {'form':form}


    return render(request, 'registration.html',context)
