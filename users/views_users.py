from django.shortcuts import render, redirect, HttpResponse 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from home.models import Book
from .forms_users import CUForm

# Create your views here.


def v_login(request):
    mode = 'log'
    if request.method == 'POST':
        uname = request.POST['txt_uname']
        passwd = request.POST['pwd_login']
        user = authenticate(username=uname,password=passwd)
        if user is not None:
            if user.is_active:
                login(request,user)
                messages.success(request, "Yeah ! you have logged in Successfuly. ")
                bk = Book.objects.all()
                context = {'pages': 'ps', 'books': bk, 'title':'Home' }
                return redirect('Home')
            else:
                messages.error(request, 'Please enter a valid username')
                return HttpResponse('Please check your Email ')
        else:
            messages.error(request, 'Please enter a valid username')
            return HttpResponse('Please check your Email ')
    return render(request,'auth.html', {'title' : 'Login', 'mode': mode })
    

def v_signin(request):
    mode = 'sign'
    form = CUForm()
    if request.method == 'POST':
        sign_form = CUForm(request.POST)
        if sign_form.is_valid():
            user = sign_form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'An error occurred while Signing in!!')
    return render(request,'auth.html', {'title' : 'Sign In', 'mode': mode, 'form' : form })


def v_profile(request):
    return render(request, 'profile.html', { 'profile' : 'In Developement' })