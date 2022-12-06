from django.shortcuts import render

# Create your views here.

def prev(request):
    return render(request,'prev.html')

def upcoming(request):
    return render(request,'upcoming.html')

