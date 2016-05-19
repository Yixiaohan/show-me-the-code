# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth import urls as auth_urls
from django.contrib import admin
from blog.views import article_view, home_page, test
from message_board import views
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home_page),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^blog$', home_page, name='blog home page'),

    url(r'^message_board$', views.message_board, name='message board'),
    url(r'^api/message_submit$', views.message_submit, name='submit messag'),

    url(r'^article$', article_view, name='article_page'),
    url(r'^home$', home_page, name='home_page'),

    url(r'^test$', test, name='test'),
)
