# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth import urls as auth_urls
from dj_test.settings import STATIC_PATH
from django.contrib import admin
from blog.views import home, article, blog, about, contact, test
from message_board import views
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^', include('django.contrib.auth.urls')),

    url(r'^$', home, name='home'),
    url(r'^home$', home, name='home'),

    url(r'^blog/$', blog, name='blog'),
    url(r'^article/(?P<pk>[0-9]+)/$', article, name='article'),
    url(r'^contact$', contact, name='contact'),
    url(r'^about$', about, name='about'),

    url(r'^message_board$', views.message_board, name='message board'),
    url(r'^api/message_submit$', views.message_submit, name='message_submit'),

    url(r'^test$', test, name='test'),

    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_PATH}),
)
