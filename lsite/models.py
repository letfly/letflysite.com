# -*-coding:utf-8 -*-
'''
Created on 2015-2-18

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django.db import models
import binascii
import os
from django.conf import settings

def str_crc32(string):
    return(hex(binascii.crc32(string.encode('utf8')))[2:])

def focus_image_upload(instance, filename):
    filename = str_crc32(instance.title) + os.path.splitext(filename)[1]
    return os.path.join(settings.FOCUS_IMAGE_ROOT, filename)

class Focus(models.Model):
    title = models.CharField(u'标题', max_length=100)
    image = models.ImageField(upload_to=focus_image_upload, verbose_name=u'配图', blank=True)
    description = models.CharField(u'描述', max_length=1000)
    created = models.DateTimeField(u'添加时间', auto_now_add=True)
    is_shown = models.BooleanField(u'是否展示', default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'lsite_focus'
        verbose_name = u'最近关注'
        verbose_name_plural = u'最近关注'
