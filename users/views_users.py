from django.shortcuts import render, redirect, HttpResponse 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
                messages.success(request, "Yeah "+user.first_name +"! You have logged in Successfuly. ")
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
            messages.success(request, "User is successfully registered")
            return redirect('Home')
        else:
            messages.error(request, 'An error occurred while Signing in!!')
    return render(request,'auth.html', {'title' : 'Sign In', 'mode': mode, 'form' : form })

@login_required(login_url="Login")
def v_profile(request):
    return render(request, 'profile.html', { 'profile' : 'In Developement' })

@login_required(login_url="Login")
def v_edit(request):
    if request.method == 'POST':
        uimg = request.FILES['profile_pic']
        ufname = request.POST['txt_ed_fname']
        ulname = request.POST['txt_ed_lname']
        umail = request.POST['txt_ed_mail']
        
        return render(request, 'Profile.html', { 'title' : 'Profile', })


def v_logout(request):
    logout(request)
    messages.success(request, "User successfully Logged out!")
    return redirect("Index")