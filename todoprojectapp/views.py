from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Register,todo
from django.contrib.auth.models import User
import datetime as dtm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('Uname')
        passwd = request.POST.get('Pass')
        print(username,passwd)
        user = authenticate(username=username,password=passwd)
        if user is not None:
            print("yes")
            if user.is_superuser:
                print("super")
                messages.warning(request, 'super user is not allowed.')
                return redirect('home')
            elif user.is_staff:
                print("staff")
                messages.warning(request, 'staff are not allowed')
                return redirect('home')
            elif user.is_active:
                print("simple user")
                login(request,user)
                messages.success(request, 'successfully login')
                return render(request,'createtodo.html')
            elif user.is_anonymous:
                print("anonymous")
                messages.warning(request,"not permission")
                return redirect('home')
            else:
                print("invalid")
            pass
           # A backend authenticated the credentials
            
        else:
            print("no")
           # No backend authenticated the credentials

    return render(request,'todo.html')

#         user = authenticate(username='john', password='secret')
# 
def logout_view(request):
    logout(request)
    messages.success(request,'successfully logout')
    return render(request,'home.html')



def register(request):
    if request.method == "POST":
        Name = request.POST.get('name')
        phone_number = request.POST.get('p_num')
        address = request.POST.get('add')
        date_of_birth = request.POST.get('dob')
        email = request.POST.get('eml')
        profile_pics = request.FILES['pic']
        passwrod1 = request.POST.get('pswd')
        password2 = request.POST.get('pswd1')
        print(Name,phone_number,address,date_of_birth,email,profile_pics,passwrod1,password2)
        if passwrod1 == password2:
            user_details = User.objects.create(username= email,email=email,first_name=Name,password=password2)
            register_details= Register(Users=user_details,Phone_number=phone_number,Address=address,DOB=date_of_birth,Image=profile_pics)
            user_details.save()
            register_details.save()
            messages.success(request,"got register")
            return redirect('home')
        else:
            messages.success(request,"password does not matched")
            return render(request,'register.html')
    return render(request,'register.html')
 

def create(request):
    if request.method == "POST":
        title = request.POST.get('ttl')
        context = request.POST.get('cnt')
        print(title,context)
        user_details = Register.objects.get(Users=request.user)
        Todo = todo(User_details=user_details,Title=title,Content= context)
        Todo.save()
        messages.success(request,'Successfully created todo.')
        return render(request, 'createtodo.html')
    return render(request,'createtodo.html')


def todolist(request):
    user_details = Register.objects.get(Users=request.user)
    Todo = todo.objects.filter(User_details= user_details)
    return render(request,'list.html',context={'todo':Todo})


def completed_todo(request):
    user_details = Register.objects.get(Users=request.user)
    Todo = todo.objects.filter(User_details= user_details,Completed = True)
    return render(request, 'completed_todo.html',context={'todo':Todo})

def edit(request,pk):
    print(pk)
    if request.method == "GET":
        Todo = todo.objects.get(id = pk)
        return render(request, 'edit.html',context={'Todo':Todo})

@login_required
def delete(request,pk):
    Todo = todo.objects.get(id = pk)
    Todo.delete()
    messages.success(request,'Successfully deleted todo.')
    return redirect('todolist')

def edit_todo(request):
    if request.method == "POST":
        id_v = request.POST.get('id_val')

        title = request.POST.get('ttl')
        context = request.POST.get('cnt')
        comp = request.POST.get('cmt')
        print(title,context,comp)
        Todo = todo.objects.get(id = int(id_v))
        Todo.Title = title
        Todo.Content = context
        if comp == "on":
            Todo.Completed = True
            Todo.Completion_date = dtm.datetime.now()
        Todo.save()
        messages.success(request,'Successfully updated todo.')
        return redirect('todolist')