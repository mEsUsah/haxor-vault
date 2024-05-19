from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'vault/home.html', context)