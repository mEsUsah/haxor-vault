from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from vault.models import App, Credential

def home(request):
    context = {}
    return render(request, 'vault/home.html', context)

@login_required(login_url="login")
def dashboard(request):
    context = {}
    return render(request, 'vault/dashboard.html', context)

@login_required(login_url="login")
def create_app(request):
    context = {}
    return render(request, 'vault/app_create.html', context)

@login_required(login_url="login")
def edit_app(request, id):
    app = App.objects.get(id=id)
    context = {
        'app': app
    }
    return render(request, 'vault/app_details.html', context)

@login_required(login_url="login")
def create_credential(request):
    context = {}
    return render(request, 'vault/credential_create.html', context)

@login_required(login_url="login")
def edit_credential(request, id):
    credential = Credential.objects.get(id=id)
    context = {
        'credential': credential
    }
    return render(request, 'vault/credential_details.html', context)