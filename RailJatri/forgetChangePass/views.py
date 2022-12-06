from django.shortcuts import render

# Create your views here.
def forgotChangepass(request):
    return render(request,'forgetchangepass.html')