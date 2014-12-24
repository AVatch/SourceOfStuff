from django.shortcuts import render
from django.views.generic import View

from items.models import Item


class BaseView(View):
    template_name = 'item_list.html'

    def get(self, request, *args, **kwargs):
        callback = {}

        # Pull the most recent items
        item_list = Item.objects.all()
        callback['item_list'] = item_list

        # Get the users twitter information
        # try:
        #     contributor = Contributor.objects.get(username=request.user)
        #     social = contributor.social_auth.get(provider='twitter')
        #     access_token = social.extra_data['access_token']
        # except Exception as e:
        #     print e

        return render(request, self.template_name, callback)
