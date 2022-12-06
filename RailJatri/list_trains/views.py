from django.shortcuts import render

def list_train(request):
    return render(request,'list_trains.html')
