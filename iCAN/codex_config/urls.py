from django.conf.urls import patterns, include, url
from django.contrib import admin
from codex import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^codex/', include('codex.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^openid/(.*)', SessionConsumer()),
)
