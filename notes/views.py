from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import *
from datetime import date


# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def user_login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    return render(request, 'login.html', {'error': error})


def signup(request):
    error = ''
    if request.method == 'POST':
        f = request.POST['first_name']
        l = request.POST['last_name']
        n = request.POST['number']
        e = request.POST['email']
        p = request.POST['password']
        b = request.POST['branch']
        r = request.POST['role']
        print(f,l,n,e,p,b,r)
        try:
            user = User.objects.create_user(username=e, password=p, first_name=f, last_name=l)
            Signup.objects.create(user=user, contact=n, branch=b, role=r)
            error = 'no'
        except:
            error = 'yes'
        print("Found Error",error)
    return render(request, 'signup.html', {'error': error})


def admin_home(request):
    if not request.user.is_staff:
        return redirect('adminlogin.html')
    return render(request, 'admin_home.html')


def adminlogin(request):
    error = ""

    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pwd']
        user = authenticate(request, username=username, password=password)

        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    return render(request, 'adminlogin.html', {'error': error})


def Logout(request):
    logout(request)
    return redirect('index')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login.html')
    user = User.objects.filter(username=request.user.username).first()
    data = Signup.objects.filter(user=user)
    print(request.user.username)
    return render(request, 'profile.html', {'user': user, 'data': data})


def changepassword(request):
    print(request.user)
    error = ""
    if not request.user.is_authenticated:
        return redirect('login.html')

    if request.method == "POST":
        old = request.POST['old']
        new = request.POST['new']
        confirm = request.POST['confirm']
        if new == confirm:
            user = User.objects.get(username__exact=request.user.username)
            user.set_password(new)
            user.save()
            error = "no"
        else:
            error = "yes"
    return render(request, 'changepassword.html', {'error': error})


def editprofile(request):
    error = ""
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)

    try:
        if request.method == "POST":
            f = request.POST['first_name']
            l = request.POST['last_name']
            c = request.POST['contact']
            b = request.POST['branch']
            user.first_name = f
            user.last_name = l
            data.contact = c
            data.branch = b
            user.save()
            data.save()
            error = 'no'
    except:
        error = 'yes'
    print(error)

    return render(request, 'editprofile.html', {'data': data, 'error': error})


def uploadnotes(request):
    error = ''
    if not request.user.is_authenticated:
        return redirect('login.html')
    if request.method == 'POST':
        b = request.POST['branch']
        s = request.POST['subject']
        n = request.FILES['notesfile']
        t = request.POST['filetype']
        d = request.POST['discription']
        u = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=u, uploadingdate=date.today(), branch=b, subject=s,
                                 notesfile=n, filetype=t, discription=d, status='pending')
            error = 'no'
        except:
            error = 'yes'

    return render(request, 'uploadnotes.html', {'error': error})

def viewmynotes(request):
    if not request.user.is_authenticated:
        return redirect('login.html')
    user = User.objects.get(id=request.user.id)
    notes=Notes.objects.filter(user=user)
    return render(request, 'viewmynotes.html', {'notes': notes})

def viewallnotes(request):
    if not request.user.is_authenticated:
        return redirect('login.html')
    users = User.objects.all()
    notes=Notes.objects.all()
    return render(request, 'viewmynotes.html', {'notes': notes,'users':users})

def delete_note(request,id):
    if not request.user.is_authenticated:
        return redirect('login.html')
    users = User.objects.all()
    note=Notes.objects.filter(id=id)
    note.delete()
    return redirect('viewmynotes')

def admin_allnotes(request):
    if not request.user.is_authenticated:
        return redirect('login.html')
    users = User.objects.all()
    notes=Notes.objects.all()
    return render(request, 'admin_allnotes.html', {'notes': notes})

def admin_delete_note(request,id):
    if not request.user.is_authenticated:
        return redirect('adminlogin.html')
    users = User.objects.all()
    note=Notes.objects.filter(id=id)
    print("id notes",notes)
    note.delete()
    return redirect('admin_allnotes')

def change_status(request,id):
    error=''
    if not request.user.is_authenticated:
        return redirect('adminlogin.html')
    notes = Notes.objects.get(id=id)
    if request.method=="POST":
        try:
            st = request.POST['status']
            notes.status = st
            notes.save()
            error='no'
        except:
            error='yes'
    return render(request,'change_status.html',{'error':error})

def admin_viewallusers(request):
    if not request.user.is_authenticated:
        return redirect('adminlogin.html')

    users=Signup.objects.all()
    return render(request,'admin_viewallusers.html',{'users':users})

def admin_deleteuser(request,id):
    if not request.user.is_authenticated:
        return redirect('adminlogin.html')
    user= User.objects.get(id=id)
    user.delete()
    user.save()
    return redirect('admin_viewallusers')

def showprofile(request):
    if not request.user.is_authenticated:
        return redirect('login.html')
    user = User.objects.get(id=request.user.id)
    print(user.last_name)
    data = Signup.objects.get(user=user)

    return render(request,'showprofile.html',{"data":data})