from django.views.generic import DetailView, View
from django.utils import timezone
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django_wysiwyg.utils import clean_html, sanitize_html

from contributors.models import Contributor

from sourceofstuff.keys import SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET

from twython import Twython

from .models import Item
from .forms import ItemForm


class ItemListView(View):
    template_name = 'item_list.html'

    def get(self, request, page=None, modifier=None, *args, **kwargs):
        callback = {}
        if modifier:
            print "using a modifier"
            item_list = Item.objects.all()
        else:
            item_list = Item.objects.all()
        # Pagination: https://docs.djangoproject.com/en/1.7/topics/pagination/
        paginated_items = Paginator(item_list, 9)
        try:
            items = paginated_items.page(page)
            callback['next_page'] = int(page) + 1
        except PageNotAnInteger:
            items = paginated_items.page(1)
            callback['next_page'] = 2
        except EmptyPage:
            items = paginated_items.page(paginated_items.num_pages)
        except Exception as e:
            print e
            items = None

        callback['item_list'] = items
        if page is None:
            callback['first_page'] = True
        #################################################################
        # This is a hack - because twitter profile pic is annoying to get
        if request.user.id is not None:
            if request.user.profile_img_url is None:
                user = Contributor.objects.get(username=request.user)
                social = user.social_auth.get(provider='twitter')
                access_token = social.extra_data['access_token']

                t = Twython(app_key=SOCIAL_AUTH_TWITTER_KEY,
                            app_secret=SOCIAL_AUTH_TWITTER_SECRET,
                            oauth_token=access_token[u'oauth_token'],
                            oauth_token_secret=access_token[u'oauth_token_secret'])

                twitter_account = t.show_user(screen_name=request.user.username)
                profile_img_url = twitter_account[u'profile_image_url']
                user.profile_img_url = profile_img_url
                user.save()
        #################################################################

        return render(request, self.template_name, callback)


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
        itemForm = ItemForm(request.POST, request.FILES)

        if itemForm.is_valid():
            item = itemForm.save(commit=False)
            item.origin_story = sanitize_html(item.origin_story)
            item.origin_story = clean_html(item.origin_story)
            item.save()
            item.contributors.add(request.user)

            # Handle the tagging
            for tag in itemForm.cleaned_data['tags']:
                item.tags.add(tag)

            return redirect('/item/'+str(item.id))
        callback['itemForm'] = itemForm  # return form with errors
        return render(request, self.template_name, callback)


class ItemEditView(View):
    template_name = 'item_edit.html'

    def get(self, request, pk, *args, **kwargs):
        callback = {}
        item = Item.objects.get(pk=pk)
        callback['item'] = item
        itemForm = ItemForm(instance=item)
        callback['itemForm'] = itemForm
        return render(request, self.template_name, callback)

    def post(self, request, pk, *args, **kwargs):
        callback = {}
        item = Item.objects.get(pk=pk)
        itemForm = ItemForm(request.POST, instance=item)
        if itemForm.is_valid():
            item = itemForm.save(commit=False)
            item.last_modified = timezone.now()
            item.save()

            # Tags
            for tag in item.tags.all():
                item.tags.remove(tag)
            for tag in itemForm.cleaned_data['tags']:
                item.tags.add(tag)

            # if this is a new contributor add them
            if Item.objects.filter(contributors__pk=request.user.pk).count() == 0:
                item.contributors.add(request.user)
            return redirect('/item/'+str(item.id))
        callback['itemForm'] = itemForm  # return form with errors
        return render(request, self.template_name, callback)


class ItemVoteView(View):
    def get(self, request, vote, pk, *args, **kwargs):
        item = Item.objects.get(pk=pk)

        if request.user in item.raters.all():
            print "User rated this, skip"
        else:
            print "User did not rate this, go on"

            if vote == 'up':
                item.upvotes += 1
                item.save()
            elif vote == 'down':
                item.downvotes += 1
                item.save()
            else:
                return redirect('/item/'+str(item.id))

            item.raters.add(request.user)

        return redirect('/item/'+str(item.id))
