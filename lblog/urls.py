from django.conf.urls import patterns,url

from lblog import views

urlpatterns = patterns('',
	url(r'^$',views.blog_home,name='blog_home'),
	url(r'^(\d+)/$', views.GetDetail.as_view(), name='blog_detail'),
	url(r'^(\d+)/comment/$', views.Comment.as_view(), name='blog_comment'),
)
