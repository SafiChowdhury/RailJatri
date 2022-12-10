from django.shortcuts import render,redirect
# from home.models import login_details
# from create_acc.models import passenger
from django.contrib.auth import authenticate,login,logout
from .forms import loginUser
# Create your views here.

def home_page(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('search_tick')
    context = {}

    return render(request,'login.html')



