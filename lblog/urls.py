# -*-coding:utf-8 -*-
'''
Created on 2015-2-5

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django.conf.urls import patterns,url

from lblog import views
from lblog.feeds import LatestBlogs

urlpatterns = patterns('',
	url(r'^$',views.blog_home,name='blog_home'),
	url(r'^(\d+)/$', views.GetDetail.as_view(), name='blog_detail'),
	url(r'^(\d+)/comment/$', views.Comment.as_view(), name='blog_comment'),
	url(r'^rss/$', LatestBlogs(), name='blog_rss'),
)
