from django.shortcuts import render
from django.views.generic import View


class ItemView(View):
    template_name = 'test.html'

    def get(self, request, *args, **kwargs):
        callback = {}
        callback['hello'] = 'world'
        return render(request, self.template_name, callback)
