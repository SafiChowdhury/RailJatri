from django.shortcuts import render

def bkash(request):
    return render(request,'bkash_payment.html')

def card(request):
    return render(request,'card_payment.html')

def nexus(request):
    return render(request,'nexus_payment.html')

def pay_cat(request):
    return render(request,'payment selection.html')

def rocket(request):
    return render(request,'rocket_payment.html')

