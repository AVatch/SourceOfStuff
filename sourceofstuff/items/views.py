from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Item


class ItemDetailView(View):
    template_name = 'item.html'

    def get(self, request, *args, **kwargs):
        callback = {}
        return render(request, self.template_name, callback)


class ItemListView(ListView):
    template_name = 'item_list.html'
    model = Item
