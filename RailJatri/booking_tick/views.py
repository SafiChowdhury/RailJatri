from django.shortcuts import render

def booking_ticket(request):
    return render(request,'search.html')

def seat_select(request):
    return render(request,'seat_selection.html')

def succesful(request):
    return render(request,'successful.html')

def tick_details(request):
    return render(request,'ticket.html')