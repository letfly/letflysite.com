# -*-coding:utf-8 -*-
'''
Created on 2015-2-28
@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

import logging
logger = logging.getLogger('letflysite')


def set_log(level, msg):
    getattr(logger, level)(msg)
