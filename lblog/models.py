# -*-coding:utf-8 -*-
'''
Created on 2015-2-5

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django.db import models
from django.db.models.expressions import F

class BaseModel(models.Model):
	name = models.CharField(u'名称', max_length=30)
	count = models.IntegerField(u'引用', default=0)
	created = models.DateTimeField(u'创建时间', auto_now_add=True)

	def __unicode__(self):
		return self.name

	def incr(self, num=1):
		self.count = F('count') + num
		self.save()

	def decr(self, num=1):
		self.count = F('count') - num
		self.save()

	class Meta:
		abstract = True
		ordering = ['-created']

class Tag(BaseModel):
	tag_name = models.CharField(max_length=20)
	create_time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.tag_name

class Category(BaseModel):

	class Meta:
		db_table = 'dblog_category'
		verbose_name = u'分类'
		verbose_name_plural = u'分类'

#class Author(models.Model):
#	name = models.CharField(max_length=30)
#	email = models.EmailField(blank=True)
#	website = models.URLField(blank=True)

#	def __unicode__(self):
#		return u'%s' % (self.name)

class Theme(BaseModel):

	class Meta:
		db_table = 'dblog_theme'
		verbose_name = u'主题'
		verbose_name_plural = u'zhuti'

class Topic(BaseModel):
	description = models.CharField(u'描述', max_length=2000, blank=True)

	class Meta:
		db_table = 'dblog_topic'
		verbose_name = u'专题'
		verbose_name_plural = u'专题'

class Blog(models.Model):
	title = models.CharField(u'标题', max_length=100)
	theme = models.ForeignKey(Theme, verbose_name=u'主题')
	category = models.ForeignKey(Category, verbose_name=u'分类')
	topic = models.ForeignKey(Topic, verbose_name=u'专题', null=True, blank=True)
	publish_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
#	author = models.ForeignKey(Author, verbose_name=u'作者')
	created = models.DateTimeField(u'创建时间', auto_now_add=True)
	updated = models.DateTimeField(u'修改时间', auto_now=True)
	tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
	content = models.TextField(u'正文')

	is_draft = models.BooleanField(u'草稿状态', default=False)
	is_published = models.BooleanField(u'公开状态', default=True)

	click_count = models.IntegerField(u'点击量', default=0, editable=False)
	comment_count = models.IntegerField(u'评论数', default=0, editable=False)
	
	#def click(self, ip_addr):
		#from core.utils import get_redis

		#cache_key = settings.BLOG_VISITORS_CACHE_KEY.format(self.id)
		#coon = get_redis()
		#if int()

	class Meta:
		
		verbose_name = u'博客'
		verbose_name_plural = u'boke'
		
