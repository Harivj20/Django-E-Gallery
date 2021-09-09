from django.shortcuts import render,redirect
from .models import Photo,Category,Theme
from .forms import Form,Forms,Themeform
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
@login_required
def gallery(request,*args,**kwargs):
    category=request.GET.get('category')
    if category==None:
         photo=Photo.objects.all()
    else:
         photo=Photo.objects.filter(category__name=category)
    
    categories=Category.objects.all()

    if Theme.objects.filter(user=request.user.username).exists():
        color=Theme.objects.get(user=request.user.username).color
    else:
        color='red'    
    context={'categories':categories,'photo':photo,'color':color}
    return render(request,'gallery.html',context)
    
def theme(request):
    color=request.GET.get('color')

    if color=='dark':
        if Theme.objects.filter(user=request.user.username).exists():
            user1=Theme.objects.get(user=request.user.username)
            user1.user=request.user.username
            user1.color='grey'
            user1.save()
        else:
            user3=Theme(user=request.user.username,color='orange')    

    elif color=='light':
        if Theme.objects.filter(user=request.user.username).exists():
            user2=Theme.objects.get(user=request.user.username)
            user2.user=request.user.username
            user2.color='light'
            user2.save()
    return redirect('/gallery')
@login_required    
def add(request):
    form=Form()
    if request.method=='POST':
        form=Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Album is added to gallery Successfullly!!')
            return redirect('/gallery')
        else:
            form=Form()
    context={'form':form}            

    return render(request,'add.html',context)    

@login_required
def photos(request,id):
    pic=Photo.objects.get(id=id)
    return render(request,'photos.html',{'upnext':pic})

@login_required
def new_category(request):
    forms=Forms()
    if request.method=='POST':
        forms=Forms(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,'New Category is added Successfully!!')
            return redirect('/add')
        else:
            forms=Forms()
    return render(request,'new_category.html',{'forms':forms})    

def searchbar(request):
    search=request.GET.get('search')
    if search==None:
       search= Photo.objects.all()
    else:
       search= Photo.objects.filter(category__name=search)  

    context={'search':search}
    return render(request,'searchbar.html',context)      

def registration(request):
    if request.method=='POST':
        username=request.POST.get('Username')
        firstname=request.POST.get('Firstname')
        lastname=request.POST.get('Lastname')
        email=request.POST.get('Email')
        password1=request.POST.get('Password1')
        password2=request.POST.get('Password2')
        gender=request.POST.get('gender')
        dob=request.POST.get('Birthday')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is already taken.')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Id is already taken.')
                return redirect('/register') 
            else:
                user=User.objects.create(username=username,email=email,first_name=firstname,last_name=lastname,password=password1)
                user.save()
                return redirect('/gallery')
        else:
            messages.warning(request,'Password Does not Match!...Please enter it again!!!!')
            return redirect('/register')               
    return render(request,'registration.html')    

def login(request):
    if request.method=='POST':
        username=request.POST.get('Username')
        password=request.POST.get('Password1')
        user=authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/gallery')
        else:
            messages.warning(request,'Invalid Credentials')  
            return redirect('/login')  

    return render(request,'login.html')        

def logout(request):
    auth.logout(request)    
    return redirect('/login')

def ThemeForm(request):
    tform=Themeform()
    if request.method=='POST':
        tform=Themeform(request.POST)
        if tform.is_valid():
            tform.save()
            return redirect('/gallery')
        else:
            tform=ThemeForm()
    return render(request,'ThemeForm.html',{'tform':tform})        
