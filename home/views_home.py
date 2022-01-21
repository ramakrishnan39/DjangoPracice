
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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


def v_logout(request):
    logout(request)
    return render(request, 'Logout.html',{'title': 'Log out'})


def v_savebook(request):
    if request.method == 'POST':
        b_name = request.POST['txt_bookname']
        a_name = request.POST['txt_authname']
        p_name = request.POST['txt_pubname']
        b_file = request.FILES['file_bk']
        p_usr = request.user
        bk = Book(book_name=b_name, author_name=a_name,
                  publication_name=p_name, posted_by=p_usr, book_file= b_file)
        bk.save()
        messages.success(request, 'Successfully uploaded the book!')
        return redirect("Home")


def m_friends(request):
    usr = User()
    return render(request, 'Friends.html', { 'title': 'Friends', 'friends':usr})


def m_profile(request):
    books = Book.objects.filter(posted_by=request.user)
    if request.method == 'GET':
        return render(request, 'Profile.html', { 'title' : 'Profile', 'books':books})
    elif request.method == 'POST':
        ufname = request.POST['txt_ed_fname']
        ulname = request.POST['txt_ed_lname']
        umail = request.POST['txt_ed_mail']
        request.user.first_name = ufname
        request.user.last_name = ulname
        request.user.umail = umail
        request.user.save()
        return render(request, 'Profile.html', { 'title' : 'Profile','books':books})


def m_edit(request):
    return render(request,'profile/')

def m_user(request, usr):
    user_post = User.objects.get(username=usr)
    cont={ 'title': 'User Profile ', 'post_user':user_post}    
    if request.method == 'POST':

        return render(request,'User_page.html', context=cont )
    elif request.method == 'GET':
        return render(request,'User_page.html', context=cont )
    else:
        cont={ 'title': 'User Profile ',}
        return render(request,'User_page.html', context=cont )
