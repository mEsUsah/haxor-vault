from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    context = {}
    return render(request, 'vault/home.html', context)