import datetime

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template.response import TemplateResponse

from django.contrib import messages

from .models import User
from datetime import datetime




def sign_in(request):
    if request.user.is_authenticated:
        return redirect('profile/')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')
        if user is None:
            messages.error(request, 'Невірно введені дані')
            return redirect('/auth')
    else:
        response = TemplateResponse(request, 'authentication/sign_in.html', {})
        return response


def sign_up(request):
    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        dob = request.POST['dob']

        if datetime.strptime(dob, "%Y-%m-%d") < datetime.now():
            user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            dob=datetime.strptime(dob, "%Y-%m-%d")
            )
            user.set_password(password)
            user.save()

            return redirect('/profile')
        else:
            messages.error(request, 'Дата народження не може бути більшою')
            return redirect('/auth/sign_up/')
    else:
        response = TemplateResponse(request, 'authentication/sign_up.html', {'sign_up_url': '/authentication/sign_up'})
        return response


def log_out(request):
    logout(request)
    return redirect('/profile')

