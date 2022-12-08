from django.shortcuts import render
from home.models import login_details
from create_acc.models import passenger

# Create your views here.

def home_page(request):
    return render(request,'login.html')

def login1(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password =request.POST.get('password')
    return render(request,'search.html')
