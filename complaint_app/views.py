from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import complaint, reply
import datetime

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            return render(request,'home.html')
        complaints=complaint.objects.all().order_by('-id')
        return render(request,'adminhome.html',{'complaints': complaints})
    return redirect('/login')

def allusers(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            users = User.objects.all().order_by('-id')
            return render(request,'adminviewusers.html',{'users': users})
    return redirect('/')

def login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
        return render(request,'login.html')
    return redirect('/')

def register(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            uname=request.POST['uname']
            password=request.POST['password']
            if User.objects.filter(username=uname).exists():
                return redirect('/register')
            user=User.objects.create_user(first_name=fname,last_name=lname, email=email, username=uname,password=password)
            auth.login(request,user)
            return redirect('/')
        return render(request,'register.html')
    return redirect('/')

def addcomplaint(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            if not request.user.is_superuser:
                subject=request.POST['subject']
                compt = request.POST['complaint']
                username=request.user.username
                submit=complaint(username=username, subject = subject, complaint = compt, date=datetime.date.today())
                submit.save()
                return redirect('/')
    return redirect('/')

def mycomplaints(request):
    if request.user.is_authenticated:
            if not request.user.is_superuser:
                username=request.user.username
                compt=complaint.objects.filter(username=username).order_by('-id')
                return render(request,'mycomplaints.html',{'complaints':compt})
    return redirect('/login')

def viewcomplaint(request,compt_id):
    if request.user.is_authenticated:
        compt = complaint.objects.get(id=compt_id)
        rply = reply.objects.filter(complaint_id = compt_id)
        return render(request,'viewcomplaint.html',{'complaint' : compt, 'replies' : rply})
    return redirect('/login')

def complaintreply(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            rply = request.POST['reply']
            compt_id = request.POST['compt_id']
            username = request.user.username
            if request.user.is_superuser:
                userstatus = 'admin'
            else:
                userstatus = 'user'
            submit=reply(username=username, complaint_id = compt_id, userstatus = userstatus, reply = rply, date=datetime.date.today())
            submit.save()
        return redirect('/viewcomplaint/'+ str(compt_id))
    return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/')