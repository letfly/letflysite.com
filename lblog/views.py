
from core.views import BaseView, AccessAuthMixin
#from django.db.models.query_utils import Q
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

#from core.models import DComment
from lblog.forms import CommentForm 
from lblog.models import Blog, Category, Tag

class BlogBase(BaseView):
	tags_shown_count = 50

	def get_context_data(self, extra_context):
		context = {
			'categories': Category.objects.exclude(count=0),
			'tags': Tag.objects.exclude(count=0).order_by('?')[:self.tags_shown_count],
			'pblogs': Blog.objects.all().order_by('-click_count', '-created')[:8],
		}
		context.update(extra_context)
		return context

def blog_home(request):
	blogs = Blog.objects.all().order_by('-publish_time')
	
	return render_to_response('lblog/index.html', {"blogs": blogs}, context_instance=RequestContext(request))

class GetDetail(BlogBase, AccessAuthMixin):
	template_name = 'lblog/detail.html'
	template_name_m = 'lblog/detail_m.html'
	max_recommended_count = 8

	def get_context_data(self, extra_context):
		context = super(GetDetail, self).get_context_data(extra_context)
		context['form'] = CommentForm()
		return context

	def get_template_names(self):
		if self.request.session.get('VIEW_MODE') == 'mobile':
			return [self.template_name_m]
		return [self.template_name]

	#def get_recommends(self, curr):
		#return Blog.objects.filter(Q(tags__in=curr.tags.all()) |
								   #Q(cate=curr.cate),
								   #is_draft=False,
								   #is_published=True).exclude(id=curr.id).distinct()[:self.max_recommended_count]

	def get(self, request, bid):
		try:
			blog = Blog.objects.get(id=bid, is_published=True, is_draft=False)
		except Blog.DoesNotExist:
			raise Http404

		#blog.click(self.get_client_ip(request))
		blog.tag_list = [tag.name for tag in blog.tags.all()]

		relates = blog.topic.blog_set.filter(is_draft=False, is_published=True).exclude(id=blog.id) if blog.topic else []

		extra_context = {
			'blog': blog,
			'relates': relates,
			#'recommends': self.get_recommends(blog),
			#'comments': DComment.objects.get_comments(blog)
		}
		return self.render_to_response(self.get_context_data(extra_context))

#def blog_detail(request,bid):
#	blog = Blog.objects.all().get(id=bid)
#	return render_to_response('lblog/detail.html', {"blog": blog}, context_instance=RequestContext(request))
	
