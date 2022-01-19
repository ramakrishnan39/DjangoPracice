from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Book, Friend

# Create your views here.

def v_index(request):
    if request.user.is_authenticated :
        return redirect("Home")
    return render(request, 'index.html', { 'title' : 'Welcome ! ', })


def v_home(request):
    bk = Book.objects.all()
    context = { 'books': bk, 'title': 'Home' }
    return render(request, 'home.html', context)

def v_savebook(request):
    if request.method == 'POST':
        return render(request, 'home.html')

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
    books = Book.objects.filter(posted_by=request.user)
    if request.method == 'GET':
        return render(request, 'Profile.html', {'pages': ps, 'title' : 'Profile', 'books':books})
    elif request.method == 'POST':
        ufname = request.POST['txt_ed_fname']
        ulname = request.POST['txt_ed_lname']
        umail = request.POST['txt_ed_mail']
        request.user.first_name = ufname
        request.user.last_name = ulname
        request.user.umail = umail
        request.user.save()
        return render(request, 'Profile.html', {'pages': ps, 'title' : 'Profile','books':books})

def m_logout(request):
    auth.logout(request)
    return render(request, 'Logout.html',{'title': 'Log out'})


def m_savebook(request):
    if request.method == 'POST':
        b_name = request.POST['txt_bookname']
        a_name = request.POST['txt_authname']
        p_name = request.POST['txt_pubname']
        b_file = request.FILES['file_bk']
        p_usr = request.user
        bk = Book(book_name=b_name, author_name=a_name,
                  publication_name=p_name, posted_by=p_usr, book_file= b_file)
        bk.save()
        bk = Book.objects.all()
        cont = {
        'pages': ps, 'books': bk, 'messege': 'Hurray ! Successfully added the book. '
        }
    return redirect(reverse('home'),context=cont)


def m_edit(request):
    return render(request,'profile/')

def m_user(request, usr):
    user_post = User.objects.get(username=usr)
    cont={'pages': ps, 'title': 'User Profile ', 'post_user':user_post}    
    if request.method == 'POST':

        return render(request,'User_page.html', context=cont )
    elif request.method == 'GET':
        return render(request,'User_page.html', context=cont )
    else:
        cont={'pages': ps, 'title': 'User Profile ',}
        return render(request,'User_page.html', context=cont )
