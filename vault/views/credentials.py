from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from vault.models import Credential

@login_required(login_url="login")
def create(request):
    context = {}
    return render(request, 'vault/credential_create.html', context)

@login_required(login_url="login")
def edit(request, id):
    credential = Credential.objects.get(id=id)
    context = {
        'credential': credential
    }
    return render(request, 'vault/credential_details.html', context)