from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from items.models import Item


class BaseView(View):
    template_name = 'item_list.html'

    def get(self, request, *args, **kwargs):
        callback = {}

        # Pull the most recent items
        item_list = Item.objects.all()

        ## Pagination: https://docs.djangoproject.com/en/1.7/topics/pagination/
        # paginated_items = Paginator(item_list, 2)
        # page = request.GET('page')
        # try:
        #     items = paginated_items.page(page)
        # except PageNotAnInteger:
        #     items = paginated_items.page(1)
        # except EmptyPage:
        #     items = paginated_items.page(paginated_items.num_pages)
        # except Exception as e:
        #     print e
        #     items = None

        callback['item_list'] = item_list

        # Get the users twitter information
        # try:
        #     contributor = Contributor.objects.get(username=request.user)
        #     social = contributor.social_auth.get(provider='twitter')
        #     access_token = social.extra_data['access_token']
        # except Exception as e:
        #     print e

        return render(request, self.template_name, callback)
