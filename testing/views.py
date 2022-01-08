from django.shortcuts import render,redirect
from testing.forms import Nameform,CredentialFOrm
from testing.models import name,signup,product
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def test(request):
    if request.method == "POST":
        form = Nameform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/test')
            except:
                pass
    else:
        form = Nameform()
    return render(request,"formh.html" , {"form":form})

def login(request):
    if request.method == "POST":
        username =request.POST['lgusername']
        password =request.POST['lgpassword']
        user =auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid username or password")
            return redirect("/login")
    else:
        return render(request,"login.html")


def creds(request):
    if request.method =="POST":
        form=CredentialFOrm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/creds')
            except:
                pass
    else:
        form =CredentialFOrm()
        return render(request,"credentials.html",{'credentials':form})

def show(request):
    Name= product.objects.all()
    return render(request,"show.html",{"Name":Name})
def edit(request,id):
    Name = product.objects.get(id=id)
    return render(request,'edit.html',{"Name":Name})
def update(request,id):
    Name = name.objects.get(id=id)
    form = Nameform(request.POST, instance=Name)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {"Name" : Name})

def destroy(request,id):
    Name= product.objects.get(id=id)
    Name.delete()
    return redirect('/')

def signup1(request):
        if request.method =="POST":
            Realname= request.POST['realname']
            Username= request.POST['username']
            sEmail= request.POST['semail']
            sPassword= request.POST['spassword']

            if User.objects.filter(username=Username).exists():
                messages.info(request,"user exists")
                return redirect("/signup")
            else:
                user= User.objects.create_user(username=Username,email=sEmail,password=sPassword,first_name=Realname)
                user.save()
                auth.login(request,user)
                print("user made")
                return redirect("/")

        else:
            form1 = signup.objects.all()
            return render(request,'Signup.html',{'signup':form1})

def logout(request):
    auth.logout(request)
    return redirect("/")

def store(request):
    p= product.objects.all()
    return render(request,'store.html',{'product':p})