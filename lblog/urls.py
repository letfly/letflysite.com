from django.conf.urls import patterns,url

from lblog import views

urlpatterns = patterns('',
	url(r'^$',views.blog_home,name='blog_home'),
	url(r'^detail/(\d+)/$',views.GetDetail.as_view(),name='blog_detail'),
)
