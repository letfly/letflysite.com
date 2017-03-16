# -*-coding:utf-8 -*-
'''
Created on 2015-2-22

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django.contrib import admin
from lblog.models import Blog, Theme, Category, Tag, Topic
from ueditor.widgets import UEditorWidget
from django.conf import settings
from django.db import models

class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'theme', 'category', 'topic', 
              'content', 'tags', 'is_draft', 'is_published']
    list_display = ['title', 'theme', 'category', 'author', 'tag_display', 'created',
                    'click_count', 'comment_count', 'is_draft', 'is_published']
    list_editable = ['is_draft', 'is_published']
    list_filter = ['theme__name', 'category__name', 'is_draft', 'created']
    search_fields = ['title', 'author__username']
    
    filter_horizontal = ['tags']

    formfield_overrides = {models.TextField: {'widget': UEditorWidget(width=1000,  file_path='downloads/',  image_path=settings.BLOG_IMAGE_URL,  scrawl_path=settings.BLOG_IMAGE_URL)}}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

    def tag_display(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])
    tag_display.short_description = u'标签'

class CAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name', 'count', 'created']

admin.site.register(Blog, BlogAdmin)
admin.site.register([Theme, Category, Tag, Topic], CAdmin)
