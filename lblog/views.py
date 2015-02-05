from django.shortcuts import render_to_response
from django.template import RequestContext

from lblog.models import Article

def blog_home(request):
	blogs = Article.objects.all().order_by('-publish_time')
	
	return render_to_response('lblog/index.html', {"blogs": blogs}, context_instance=RequestContext(request))
