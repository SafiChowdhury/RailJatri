from django.shortcuts import render
from booking_tick.models import ticket_info



def card(request):
    return render(request,'card_payment.html')

def nexus(request):
    return render(request,'nexus_payment.html')



def rocket(request):
    return render(request,'rocket_payment.html')

