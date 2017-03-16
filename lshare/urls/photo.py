# -*-coding:utf-8 -*-
'''
Created on 2015-3-16

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django.conf.urls import patterns, url 
from lshare.views import GetPhotoHome

urlpatterns = patterns('',
    url(r'^$', GetPhotoHome.as_view(), name='photo_home'),
)
