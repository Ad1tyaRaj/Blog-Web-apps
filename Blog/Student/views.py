from django.shortcuts import render
from .models import User
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.



def Sign_up(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Age = request.POST['age']
        Email = request.POST['email']
        Password = request.POST['password']

        my_user = User.objects.create_user(Name,Email,Password)
        my_user.save()
        return HttpResponseRedirect('/Student/login/')

        # new_register = User(name = Name,age =Age,email =Email,password = Password)
        # new_register.save()

    return render(request,'Student/Registration.html')



def Login(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username , password = password)

            if user is not None:
                login(request,user)

                return HttpResponseRedirect('/Student/profile/')
            else:
                return HttpResponse('Your Username and Password are Incorrect!!!')

        return render(request,'Student/Login.html')
    else:
        return HttpResponseRedirect('/Student/profile/')


def Profile(request):
    if request.user.is_authenticated:
        return render(request,'Student/Profile.html')
    else:
        return HttpResponseRedirect('/Student/login/')


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/Student/login/')


