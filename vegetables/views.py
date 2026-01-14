from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
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

    if request.method == 'POST':
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        image = request.FILES.get('image')
        category_name = request.POST.get('category')
        # get or create category object
        category_obj, created = Category.objects.get_or_create(
            name=category_name
        )


        queryset.receipe_name=receipe_name,
        queryset.receipe_description=receipe_description,
        queryset.category=category_obj

        if request.FILES.get('image'):
            queryset.image = image
        
        queryset.save()

        return redirect('getAllReceipe')

    context = {'receipe' : queryset}
    return render(request,'UpdateReceipe.html',context)



def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username ")
            return redirect('login')
        
        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request, "Invalid Password")
            return redirect('login')
        else:
            login(request,user)
            return redirect('getAllReceipe')

    return render(request,'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username Already Taken ")
            return redirect('register')

        user = User.objects.create(
            first_name=first_name,
            last_name = last_name,
            username= username
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully ")

        return redirect('login')


    return render(request,'register.html')