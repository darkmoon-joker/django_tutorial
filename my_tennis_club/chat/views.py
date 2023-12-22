from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import userRegisterationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatLog

import json

# Create your views here.

def custome_404(request, exception=None):
    return render(request, '404.html', status=404)

def new_data(request):
    if request.method == 'POST':
        # Parse the JSON data sent from the frontend
        try:
            data = json.loads(request.body)
            data_value = data.get('data')

            newInstance = ChatLog(
                user_id_id = data_value.user_id,
                chat_id = data_value.chat_id,
                chat_date = data_value.chat_date,
                chat_title = data_value.chat_title,
                header = data_value.header,
                role = data_value.role,
                prompt = data_value.chat_prompt,
            )
            newInstance.save()

            result = {'status': 'success', 'message': f'Data received: {data_value}'}
        except json.JSONDecodeError:
            result = {'status': 'error', 'message': 'Invalid JSON data'}
    else:
        result = {'status': 'error', 'message': 'Invalid request method'}

    return JsonResponse(result)


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

