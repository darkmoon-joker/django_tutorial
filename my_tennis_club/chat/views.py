from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import userRegisterationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.

def custome_404(request, exception=None):
    return render(request, '404.html', status=404)

def chat_view(request):

    return render(request, 'containers/chat/home.html')

def register(request):
    if request.method == 'POST':
        form = userRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = userRegisterationForm()

    return render(request, 'containers/registeration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    
    else:
        form = AuthenticationForm()
    
    return render(request, 'containers/registeration/login.html', {'form': form})

