# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth import urls as auth_urls
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^message_board$', 'message_board.views.message_board', name='message board'),
    url(r'^api/message_submit$', 'message_board.views.message_submit', name='submit messag'),
    url(r'^test$', 'message_board.views.test', name='test page'),
)
