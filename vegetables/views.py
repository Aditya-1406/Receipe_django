from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def getAllReceipe(request):

    queryset = Receipe.objects.all()
    context = {'receipe' : queryset}

    return render(request,'AllReceipe.html',context= context)

def addReceipe(request):

    if request.method == 'POST':
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        image = request.FILES.get('image')

        category_name = request.POST.get('category')

        # get or create category object
        category_obj, created = Category.objects.get_or_create(
            name=category_name
        )

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            image=image,
            category=category_obj
        )

        return redirect('getAllReceipe')  # use URL name

    return render(request, 'CreateReceipe.html')

def deleteReceipe(request,id):
    queryset = Receipe.objects.get(id=id)

    queryset.delete()
    return redirect('getAllReceipe')

def updateReceipe(request,id):
    queryset = Receipe.objects.get(id=id)

    


