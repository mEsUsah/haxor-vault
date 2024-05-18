from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import JsonResponse
from users.models import User
from users.forms import UserForm
from users.recaptcha import validate_captcha_token

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        captchaToken = request.POST['captchaToken']
        
        valid_captcha = validate_captcha_token(captchaToken)
        if not valid_captcha:
            return JsonResponse({
                'message': "Captcha validation failed",
                "registered": False,
                "error": "captcha-failed"
            }, status=400)

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
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        passwordConfirm = request.POST['passwordConfirm']
        captchaToken = request.POST['captchaToken']

        if User.objects.filter(email=email).exists():
            return JsonResponse({
                'message': "User already exists",
                "registered": False,
                "error": "user-exists"
            }, status=400)
        
        if password != passwordConfirm:
            return JsonResponse({
                'message': "Passwords do not match",
                "registered": False,
                "error": "password-mismatch"
            }, status=400)
        
        valid_captcha = validate_captcha_token(captchaToken)
        if not valid_captcha:
            return JsonResponse({
                'message': "Captcha validation failed",
                "registered": False,
                "error": "captcha-failed"
            }, status=400)
            
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.password_hash = password
            user.is_active = 0
            # user.save()

            return JsonResponse({
                "message": "successfully registered user",
                "registered": True
            }, status=200)
        else:
            return JsonResponse({
                'message': "validation error",
                'errors': form.errors, 
            }, status=400)

    return render(request, 'users/register.html')

def logout_user(request):
    logout(request)
    return redirect('login')