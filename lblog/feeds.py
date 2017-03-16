# -*-coding:utf-8 -*-
'''
Created on 2015-2-13

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django.contrib.syndication.views import Feed

from lblog.models import Blog
from django.utils.html import strip_tags

class LatestBlogs(Feed):
    title = u'博客 - LetflySit'
    link = '/blog/rss'
    description = u'博客 - LetflySite'

    def items(self):
        return Blog.objects.filter(is_draft=False, is_published=True).order_by('-created')[:10]

    def item_title(self, item):
        return item.title
    
    def item_pubdate(self, item):
        return item.created

    def item_link(self, item):
        link = '/blog/{0}'.format(item.id)
        return link
    
    def item_description(self, item):
        description_formated = strip_tags(item.content)
        return description_formated
