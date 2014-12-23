from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import UserCreateForm


def join_view(request):
    user_form = UserCreateForm(request.POST)
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
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
