#coding:utf8
'''
Created on 2015-2-10

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django.contrib.comments.models import Comment
from django.contrib.comments.managers import CommentManager
from django.db import models

class DCommentManager(CommentManager):
	def get_comments(self, obj):
		try:
			obj_type = ContentType.objects.get_for_model(obj)
			return self.filter(content_type=obj_type, objects_pk=obj.pk, related=None, is_public=True)
		except:
			return []

	def get_target_comment(self, cmt_id):
		try:
			return self.get(id=cmt_id)
		except:
			return None
	
class DComment(Comment):
	related = models.ForeignKey('DComment', null=True, blank=True, related_name='related_comment')
	mail_reply = models.BooleanField(u'接受回复邮件', default=True)
	objects = DCommentManager()

	def get_replys(self):
		return self.related_comment.all()
