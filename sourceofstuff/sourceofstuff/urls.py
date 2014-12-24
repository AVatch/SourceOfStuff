from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import BaseView
from items.views import ItemDetailView, ItemCreateView

urlpatterns = patterns('',
    url(r'^$', BaseView.as_view()),

    url(r'^join$', 'contributors.views.join_view'),
    url(r'^authenticate$', 'contributors.views.authenticate_view'),
    url(r'^logout$', 'contributors.views.logout_view'),
    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^item/(?P<pk>\d+)/$', ItemDetailView.as_view(), name="item-detail"),
    url(r'^item/create/$', ItemCreateView.as_view(), name="item-create"),

    url(r'^admin/', include(admin.site.urls)),
)
