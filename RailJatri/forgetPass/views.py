from django.shortcuts import render

# Create your views here.
def forgetPass(request):
    return render(request,'forgetpass.html')