from django.shortcuts import render

# Create your views here.
def prev(request):
    return render(request,'prev.html')
