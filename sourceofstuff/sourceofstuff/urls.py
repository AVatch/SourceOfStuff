from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import BaseView
# from items.views import ItemView

urlpatterns = patterns('',
    url(r'^$', BaseView.as_view()),

    url(r'^join$', 'contributors.views.join_view'),
    url(r'^authenticate$', BaseView.as_view()),
    url(r'^logout$', 'contributors.views.logout_view'),

    url(r'^admin/', include(admin.site.urls)),
)
