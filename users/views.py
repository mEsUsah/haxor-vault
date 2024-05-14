from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import JsonResponse

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is None:
            return JsonResponse({
                "message": "Wrong username or password",
                "authenticated": False
            }, status=200)
        else:
            login(request, user)
            return JsonResponse({
                "message": "successfully signed in",
                "authenticated": True
            }, status=200)
    
    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'users/login.html')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'users/register.html')

def logout_user(request):
    logout(request)
    return redirect('login')