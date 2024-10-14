from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username = username):
            messages.error(request, "Username already exist!")
            return redirect('register')
            
        if User.objects.filter(email = email):
            messages.error(request, "Email already exist!")
            return redirect('register')
        
        if not username.isalnum():
            messages.error(request, "The usename must be Alpha-Numeric")
            return redirect('register')    
        
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, "Your account has been created successfully!")
        return redirect('login')
        
    return render(request, 'register.html', {})


def Login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        
        else:
            return HttpResponse('Error, user does not exist!')
        
    return render(request, 'login.html', {})
    

def logoutuser(request):
    logout(request)
    return redirect('login')