from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from vault.models import App, Credential

# Create your views here.
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
    app = Credential.objects.get(id=id)
    context = {
        'app': app
    }
    return render(request, 'vault/credential_details.html', context)