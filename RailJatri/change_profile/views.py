from django.shortcuts import render

def changeEmail(request):
    return render(request,'changemail.html')

def changenum(request):
    return render(request,'changenum.html')

def changePass(request):
    return render(request,'changepass.html')

def updateInfo(request):
    return render(request,'updateinfo.html')