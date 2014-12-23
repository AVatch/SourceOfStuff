from django.conf.urls import patterns, include, url
from django.contrib import admin

from items.views import ItemView

urlpatterns = patterns('',
    url(r'^$', ItemView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
