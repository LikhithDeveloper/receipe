from django.shortcuts import render,redirect
from .models import Receipe
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/register/")
def receipe(request):
    if request.method == "POST":

        data=request.POST
        receipe_name=data.get('receipe_name')
        recepie_description=data.get('recepie_description')
        receipe_image=request.FILES.get('receipe_image')
        #print(receipe_name)
        #print(recepie_description)
        #print(receipe_image)
        Receipe.objects.create(
            receipe_name = receipe_name,
            recepie_description = recepie_description,
            receipe_image = receipe_image
            )
        return redirect('/receipe/')
    
    queryset = Receipe.objects.all()
    context={'receipe':queryset}
    return render(request,'receipe.html',context)


def delete_receipe(request, id):
    queryset=Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipe/')

def update_receipe(request,id):
    queryset=Receipe.objects.get(id = id)

    if request.method == "POST":

        data=request.POST
        receipe_name=data.get('receipe_name')
        recepie_description=data.get('recepie_description')
        receipe_image=request.FILES.get('receipe_image')

        queryset.receipe_name=receipe_name
        queryset.recepie_description=recepie_description
        #queryset.receipe_image=receipe_image

        if receipe_image:
            queryset.receipe_image=receipe_image

        queryset.save()
        return redirect('/receipe/')
        
    context={'receipe':queryset}
    return render(request,'update_receipe.html',context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(request , username=username, password=password)
        if authenticate(request , username=username, password=password) is not None:
            login(request, user)
            return redirect('/receipe/')
        
        else:
            messages.info(request, 'Invalid Password')
            return redirect('/login/') 
    
    return render(request, 'login.html')


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username already exist')
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            
        )

        user.set_password(password)
        print(password)
        user.save()

        messages.info(request, 'Account Created Successfully')

        return redirect('/register/')

    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')
