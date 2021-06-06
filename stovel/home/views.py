from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Book
from . import models
# Create your views here.

ps = {
    'Home': '../home/',
    'Profile': '../profile/',
    'Friends': '../friends/',
    'Logout': '../logout/',
}


def m_index(request):
    mess = messages.get_messages(request) if messages.get_messages(request) else ['Welcome',]
    # context = {
    #     'messeges' :  mess,
    # }
    return render(request, 'Welcome_page.html', { 'title' : 'Welcome ! ', 'messeges' :  mess })


def m_home(request):
    bk = Book.objects.all()
    context = {'pages': ps, 'books': bk, 'title': 'Home' }
    return render(request, 'Home_page.html', context)


def m_login(request):
    if request.method == 'POST':
        uname = request.POST['txt_uname']
        passwd = request.POST['pwd_login']
        print(f"{uname} : {passwd}" )
        user = authenticate(username=uname,password=passwd)
        print(user)
        if user is not None:
            if user.is_active:
                login(request,user)
                messages.success(request, "Yeah ! you have logged in Successfuly. ")
                bk = Book.objects.all()
                context = {'pages': ps, 'books': bk, 'title':'Home' }
                return redirect(reverse('home'),context=context)
            else:
                messages.error(request, 'Please enter a valid username')
                return HttpResponse('Please check your Email ')
        else:
            messages.error(request, 'Please enter a valid username')
            return HttpResponse('Please check your Email ')
    elif request.method == 'GET':
        return render(request,'registration/login.html', {'title' : 'Login' })

def m_signin(request):
    if request.method == 'POST':
        ufname = request.POST['txt_first_name']
        ulname = request.POST['txt_last_name']
        passwd = request.POST['pwd_usr_passwd']
        umail = request.POST['user_email']
        username = request.POST['txt_u_name']
        udob = request.POST['dt_dob']
        if User.objects.filter(username = username).exists():
            messages.info(request,'Username is taken')
        elif User.objects.filter(email=umail).exists():
            messages.info(request,'Email is taken')
        else:
            usr = User(username=username, password=passwd,first_name=ufname,last_name = ulname,email=umail)
            usr.save()
            messages.info(request,'Successfully signed in! Please use the login window to login now...')
        return redirect(reverse('index'))
    else:
        return render(request,'registration/register.html', {'title': 'Sign In '})


def m_friends(request):
    usr = User()
    return render(request, 'Friends.html', {'pages': ps, 'title': 'Friends', 'friends':usr})


def m_profile(request):
    return render(request, 'Profile.html', {'pages': ps, 'title' : 'Profile'})


def m_logout(request):
    auth.logout(request)
    return render(request, 'Logout.html',{'title': 'Log out'})


def m_savebook(request):
    if request.method == 'POST':
        b_name = request.POST['txt_bookname']
        a_name = request.POST['txt_authname']
        p_name = request.POST['txt_pubname']
        bk = Book(book_name=b_name, author_name=a_name,
                  publication_name=p_name)
        bk.save()
        bk = Book.objects.all()
        cont = {
        'pages': ps, 'books': bk, 'messege': 'Hurray ! Successfully added the book. '
        }
    return redirect(reverse('home'),context=cont)


def m_edit(request):

    return render()