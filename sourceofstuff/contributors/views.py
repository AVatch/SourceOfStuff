from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import UserCreateForm


def join_view(request):
    callback = {}
    user_form = UserCreateForm(request.POST)
    callback['user_form'] = user_form
    if user_form.is_valid():
        username = user_form.clean_username()
        password = user_form.clean_password2()
        user_form.save()
        user = authenticate(username=username,
                            password=password)
        login(request, user)
        return redirect('/')
    return redirect('/')


def authenticate_view(request):
    callback = {}
    return redirect('/')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
