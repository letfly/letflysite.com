# -*-coding:utf-8 -*-
'''
Created on 2015-2-18

@author: Letfly<letfly@outlook.com>
LetflyWork Project
'''

from django.views.generic.base import TemplateView
from lsite.models import Focus
from lblog.models import Blog, Category
import random

class Index(TemplateView):
	template_name = 'index.html'
	template_name_mobile = 'index_m.html'

	def get_template_names(self):
		if self.request.session.get('VIEW_MODE') == 'mobile':
			return [self.template_name_mobile]
		return [self.template_name]
	
	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)

		focuses = Focus.objects.filter(is_shown=True).order_by('?')
		context['focus'] = focuses[0] if focuses.exists() else None

		blogs = Blog.objects.filter(is_published=True, is_draft=False).order_by('-created')
		context['hottest_cates'] = Category.objects.all().order_by('-count')[:5]
		context['latest_blogs'] = blogs[:5]
		#context['hottest_blogs'] = random.sample(Blog.objects.all().order_by('-click_count', '-created')[:15], blogs.count() if blogs.count() < 5 else 5)
		#context['hottest_blogs'] = blogs.order_by('-click_count')[:5]
		context['hottest_blogs'] = Blog.objects.filter(is_published=True, is_draft=False).order_by('-click_count','-created')[:5]

		#photos = Photo.objects.all()[:4]
		#if photos.count() == 4:
			#context['latest_photo'] = photos[0]
			#context['photos'] = [os.path.basename(photo.image.name) for photo in photos]
		return context
