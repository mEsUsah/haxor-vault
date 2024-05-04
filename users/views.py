from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Username or Password was wrong')
        else:
            login(request, user)
            if (request.GET.get('next')):
                return redirect(request.GET.get('next'))
            # else:
            #     return redirect('dashboard')
    

    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'Logged out')
    return redirect('login')