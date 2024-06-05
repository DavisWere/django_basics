from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from core .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from core .forms import CustomUserCreationForm, StudentMakrsForm, CustomUserRegistrationForm




def home(request):
    return render(request, 'home.html')


# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'user_profile/')  # Redirect to user profile page after successful creation
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_profile.html', {'form': form})

def Student_marks(request):
    if request.method == 'POST':
        form = StudentMakrsForm(request.POST,request.Files)
        if  form.is_valid():
            form.save()
            return redirect('student-marks')
        else :
            form = StudentMakrsForm()
        return  render (request,"user_form.html",{"form":form})

# @login_required
   
def Display_users(request):
    user = request.user
    if user is  not None:
        if user.is_superuser:
            users = CustomUser.objects.all
            context={'users':users}
            return render(request,'display_users.html',context)
        else:
            return redirect("home/")  
    else:
        return redirect("login")
    
@login_required   
def Dashboard(request ):
    user =request.user
    if user is not None:
        if user.user_type == 'employee':
            users = CustomUser.objects.filter(user_type ='employee')
            return render(request,'employee_dashboard.html','employee')
        else: 
            return render(request,'employer_dashboard.html')
    else:
        return redirect('/login')


    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/users')  # Redirect to page user
            
            else:
                # Invalid username or password, show error message
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            # Redirect to a success page or login page
            return redirect('/login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
