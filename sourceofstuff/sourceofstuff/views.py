from django.shortcuts import render
from django.views.generic import View

from contributors.forms import UserCreateForm, UserAuthForm
from items.models import Item


class BaseView(View):
    template_name = 'item_list.html'

    def get(self, request, *args, **kwargs):
        callback = {}

        # Generate the authentication forms
        user_create_form = UserCreateForm()
        callback['user_create_form'] = user_create_form
        user_auth_form = UserAuthForm()
        callback['user_auth_form'] = user_auth_form

        # Pull the most recent items
        item_list = Item.objects.all()
        callback['item_list'] = item_list

        return render(request, self.template_name, callback)
