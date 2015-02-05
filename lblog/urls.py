from django.conf.urls import patterns,url

from lblog import views

urlpatterns = patterns('',
	url(r'^$',views.blog_home,name='blog_home'),
)
