from django.views.generic import DetailView, View
from django.utils import timezone
from django.shortcuts import render

from .models import Item
from .forms import ItemForm


class ItemDetailView(DetailView):
    template_name = 'item.html'
    queryset = Item.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(ItemDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        return context


class ItemCreateView(View):
    template_name = 'item_create.html'

    def get(self, request, *args, **kwargs):
        print "GET"
        callback = {}
        itemForm = ItemForm()
        callback['itemForm'] = itemForm
        return render(request, self.template_name, callback)

    def post(self, request, *args, **kwargs):
        print "POST"
        callback = {}
        return render(request, self.template_name, callback)
