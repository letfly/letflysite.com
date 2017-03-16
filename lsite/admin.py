# -*-coding:utf-8 -*-
'''
Created on 2015-2-19

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django.contrib import admin
from lsite.forms import FocusForm
from core.widgets import AdminImageWidget
from django.db import models
from lsite.models import Focus
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect

class FocusAdmin(admin.ModelAdmin):
    forms = FocusForm
    fields = ['title', 'description', 'image']
    list_display = ['title', 'description', 'created', 'shown']
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }

    def get_urls(self):
        from django.conf.urls import patterns, url
        info = self.model._meta.app_label, self.model._meta.module_name
        return patterns('',
                        url(r'^(\d+)/shown/$',
                            self.admin_site.admin_view(self.set_shown),
                            name='%s_%s_shown' % info),
                        url(r'^(\d+)/unshown/$',
                            self.admin_site.admin_view(self.set_unshown),
                            name='%s_%s_unshown' % info)
                    ) + super(FocusAdmin, self).get_urls()

    def set_shown(self, request, object_id, from_url=''):
        focus = get_object_or_404(self.queryset(request), pk=object_id)
        focus.is_shown = True
        focus.save()

        return HttpResponseRedirect(from_url or reverse('admin:lsite_focus_changelist'))

    def set_unshown(self, request, object_id, from_url=''):
        focus = get_object_or_404(self.queryset(request), pk=object_id)
        focus.is_shown = False
        focus.save()

        return HttpResponseRedirect(from_url or reverse('admin:lsite_focus_changelist'))
    
    def shown(self, obj):
        if obj.is_shown:
            return u'<a href="{0}">取消展示</a>'.format(reverse('admin:lsite_focus_unshown', args=[obj.id]))
        return '<a href="{0}">展示</a>'.format(reverse('admin:lsite_focus_shown', args=[obj.id]))
    shown.short_description = u'是否展示'
    shown.allow_tags = True

admin.site.register(Focus, FocusAdmin)
