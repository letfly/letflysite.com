# -*-coding:utf-8 -*-
'''
Created on 2015-2-19

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            output.append('<a href="%s" target="_blank"><img src="%s" width=200 /></a>'
                        % (image_url, image_url))
        output.append(super(AdminFileWidget,
                            self).render(name, value, attrs))
        return mark_safe(u''.join(output))
