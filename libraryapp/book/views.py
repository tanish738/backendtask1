from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def book(request):
    books=Book.objects.filter(user=request.user)
    form=BookCreate()
    if request.method=="POST":
        form=BookCreate(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect('book')
        
    context={"form":form,"books":books}
    return render(request,"tasks/basic.html",context)

def register_page(request):
    form=CreateUserForm()
    data=0
    if request.method=="POST":
        #print(request.POST)
        form=CreateUserForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.POST)
            form.save()
            user=form.cleaned_data.get("email")
            messages.success(request,"Account was created created for "+user)
            return redirect('login/')
    context={"form":form,"data":data}
    return render(request,"tasks/register.html",context)

def login_page(request):
    if request.method=="POST":
        #print(request.POST.get("email"))
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect("book")
        else:
            messages.info(request,"Email of Password is incorrect")
    context={}
    return render(request,"tasks/login.html",context)

def logout_page(request):
    logout(request)
    print(request)
    return redirect('login')


def updateTask(request,pk):
    books=Book.objects.get(id=pk)
    form=BookCreate(instance=books)
    id=pk
    if request.method=="POST":
        form=BookCreate(request.POST,instance=books)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={"id":id,"form":form}
    return render(request,"tasks/update_task.html",context)

def deleteTask(request,pk):
    books=Book.objects.get(id=pk)
    form=BookCreate(instance=books)
    context={"books":books}
    if request.method=="POST":
        books.delete()
        return redirect('/')
    return render(request,"tasks/delete.html",context)
