from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate

from contributors.forms import UserCreateForm


class BaseView(View):
    template_name = 'test.html'

    def get(self, request, *args, **kwargs):
        callback = {}
        user_form = UserCreateForm()
        callback['user_form'] = user_form
        return render(request, self.template_name, callback)
