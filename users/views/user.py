from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from users.models import User
from users.forms import UserForm
from users.recaptcha import validate_captcha_token
from users.send_verification_mail import send_verification_email

def login(request):
    """ Handles the login process. 

    Redirect to dashboard if user is already authenticated,
    """

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
                "status": "username-password-mismatch",
            }, status=200)
        
        if user.is_active != 1:
            return JsonResponse({
                "message": "User account not verified",
                "status": "not-verified"
            }, status=200)
        
        login(request, user)
        return JsonResponse({
            "message": "Successfully signed in",
            "status": "authenticated",
        }, status=200)
    
    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'users/login.html')

def register(request):
    """ Handles the registration process.
    """
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        passwordConfirm = request.POST['passwordConfirm']
        captchaToken = request.POST['captchaToken']

        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({
                'message': "Invalid email",
                "registered": False,
                "error": "invalid-email"
            }, status=400)

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
            user.save()
            send_verification_email(user)

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

def logout(request):
    """ Logs out the user.
    """
    
    logout(request)
    return redirect('login')

def verify(request, id: str):
    """ Handles the user verification process."""
    
    context = {
        'status_message': None,
        'status_type': None
    }
    try:
        user = User.objects.get(verification_code=id)
    except (ValidationError, User.DoesNotExist):
        context['status_message'] = "❌Invalid verification code"
        context['status_type'] = "error"
        return render(request, 'users/verify.html', context, status=404)
    
    if user.is_active != 1:
        user.is_active = 1
        user.save()

    context['status_message'] = "🔥 User acccount verified"
    context['status_type'] = "success"
    
    return render(request, 'users/verify.html', context)
