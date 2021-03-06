from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from items.views import ItemDetailView, ItemCreateView, \
    ItemListView, ItemEditView, ItemVoteView

urlpatterns = patterns('',
    url(r'^$', ItemListView.as_view(), name="home"),

    url(r'^join$', 'contributors.views.join_view'),
    url(r'^authenticate$', 'contributors.views.authenticate_view'),
    url(r'^logout$', 'contributors.views.logout_view'),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^item/(?P<pk>\d+)/$', ItemDetailView.as_view(), name="item-detail"),
    url(r'^item/list/(?P<page>\d+)/$', ItemListView.as_view(), name="item-list"),
    url(r'^item/create/$', ItemCreateView.as_view(), name="item-create"),
    url(r'^item/edit/(?P<pk>\d+)/$', ItemEditView.as_view(), name="item-edit"),
    url(r'^item/vote/(?P<vote>[a-z]+)/(?P<pk>\d+)/$', ItemVoteView.as_view(), name="item-vote"),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
