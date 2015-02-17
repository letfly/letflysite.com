# -*-coding:utf-8 -*-
'''
Created on 2015-2-5

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django.conf.urls import patterns,url

from lblog.views import GetHome, GetDetail, Comment
from lblog.feeds import LatestBlogs

urlpatterns = patterns('',
	url(r'^$', GetHome.as_view(), name='blog_home'),
	url(r'^(\d+)/$', GetDetail.as_view(), name='blog_detail'),
	url(r'^(\d+)/comment/$', Comment.as_view(), name='blog_comment'),
	url(r'^rss/$', LatestBlogs(), name='blog_rss'),
)
