from django.shortcuts import render,redirect
from testing.forms import Nameform,CredentialFOrm,loginForm,Signupform
from testing.models import name,signup
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
        form =loginForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/login')
            except:
                pass
    else:
        form =loginForm()
        return render(request,"login.html",{'login':form})


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
    Name= name.objects.all()
    return render(request,"show.html",{"Name":Name})
def edit(request,id):
    Name = name.objects.get(id=id)
    return render(request,'edit.html',{"Name":Name})
def update(request,id):
    Name = name.objects.get(id=id)
    form = Nameform(request.POST, instance=Name)
    if form.is_valid():
        form.save()
        return redirect("/sh")
    return render(request, 'edit.html', {"Name" : Name})

def destroy(request,id):
    Name= name.objects.get(id=id)
    Name.delete()
    return redirect("/sh")

def signup1(request):
        form1 = signup.objects.all()
        return render(request,'Signup.html',{'signup':form1})
