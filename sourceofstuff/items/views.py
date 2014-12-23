from django.views.generic import DetailView
from django.utils import timezone

from contributors.forms import UserCreateForm, UserAuthForm
from .models import Item


class ItemDetailView(DetailView):
    template_name = 'item.html'
    queryset = Item.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(ItemDetailView, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        print "HERE IS GETTING THE OBKECT"
        # Return the object
        return object

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ItemDetailView, self).get_context_data(**kwargs)

        # Add the authentication forms
        user_create_form = UserCreateForm()
        context['user_create_form'] = user_create_form
        user_auth_form = UserAuthForm()
        context['user_auth_form'] = user_auth_form
        return context
