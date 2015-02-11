# -*-coding:utf-8 -*-
'''
Created on 2015-2-7 00:46

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django.conf import settings
from django.views.generic.base import TemplateResponseMixin, View
from django.http.response import HttpResponseForbidden, HttpResponseServerError, Http404

class BaseView(TemplateResponseMixin, View):
    is_ajax_required = False

    def dispatch(self, request, *args, **kwargs):
        handler = getattr(self, request.method.lower(), None)
        if not request.method.lower() in self.http_method_names or not handler:
            return self.http_method_not_allowed(request)

        if self.is_ajax_required and not request.method == 'GET' and not request.is_ajax():
            return HttpResponseForbidden()

        preloader = getattr(self, 'preloader', None)
        if preloader:
            response = preloader(request, *args, **kwargs)
            if response:
                return response

        return handler(request, *args, **kwargs)

class AccessAuthMixin(object):
    allowed_ips = getattr(settings, 'ALLOWED_IPS', [])

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def is_access_allowed(self, request):
        return self.get_client_ip(request) in self.allowed_ips
