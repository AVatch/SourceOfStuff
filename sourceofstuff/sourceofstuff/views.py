from django.shortcuts import render
from django.views.generic import View

from contributors.forms import UserCreateForm, UserAuthForm


class BaseView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        callback = {}
        user_create_form = UserCreateForm()
        callback['user_create_form'] = user_create_form
        user_auth_form = UserAuthForm()
        callback['user_auth_form'] = user_auth_form
        return render(request, self.template_name, callback)
