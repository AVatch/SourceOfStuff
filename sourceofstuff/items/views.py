from django.views.generic import DetailView, View
from django.utils import timezone
from django.shortcuts import render, redirect

from django_wysiwyg.utils import clean_html, sanitize_html

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
        # Clean the html
        object.origin_story = clean_html(object.origin_story)
        # Return the object
        return object

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        return context


class ItemCreateView(View):
    template_name = 'item_create.html'

    def get(self, request, *args, **kwargs):
        callback = {}
        itemForm = ItemForm()
        callback['itemForm'] = itemForm
        return render(request, self.template_name, callback)

    def post(self, request, *args, **kwargs):
        callback = {}
        itemForm = ItemForm(request.POST)
        if itemForm.is_valid():
            item = itemForm.save(commit=False)
            item.origin_story = sanitize_html(item.origin_story)
            item.origin_story = clean_html(item.origin_story)
            item.save()
            item.contributors.add(request.user)
            return redirect('/item/'+str(item.id))
        return render(request, self.template_name, callback)


class ItemEditView(View):
    template_name = 'item_edit.html'

    def get(self, request, pk, *args, **kwargs):
        callback = {}
        item = Item.objects.get(pk=pk)
        itemForm = ItemForm(instance=item)
        callback['itemForm'] = itemForm
        return render(request, self.template_name, callback)

    def post(self, request, *args, **kwargs):
        callback = {}
        itemForm = ItemForm(request.POST)
        if itemForm.is_valid():
            item = itemForm.save(commit=False)
            item.last_modified = timezone.now()
            item.save()
            # if this is a new contributor add them
            if item.contributors.count(request.user) == 0:
                item.contributors.add(request.user)
            return redirect('/item/'+str(item.id))
        return render(request, self.template_name, callback)
