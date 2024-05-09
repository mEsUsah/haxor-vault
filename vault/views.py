from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    context = {
    }
    return render(request, 'vault/dashboard.html', context)

@login_required(login_url="login")
def create_app(request):
    context = {
    }
    return render(request, 'vault/app_form.html', context)