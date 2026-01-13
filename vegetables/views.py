from django.shortcuts import render
from .models import *

# Create your views here.

def getAllReceipe(request):

    queryset = Receipe.objects.all()
    context = {'receipe' : queryset}

    return render(request,'AllReceipe.html',context= context)