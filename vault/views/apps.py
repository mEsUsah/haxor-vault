from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from vault.models import App

@login_required(login_url="login")
def list(request):
    context = {}
    return render(request, 'vault/dashboard.html', context)

@login_required(login_url="login")
def create(request):
    context = {}
    return render(request, 'vault/app_create.html', context)

@login_required(login_url="login")
def edit(request, id):
    app = App.objects.get(id=id)
    context = {
        'app': app
    }
    return render(request, 'vault/app_details.html', context)
