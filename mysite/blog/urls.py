from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
	# (?P<pk>[0-9]+) Means django will take everything that you place here and
	# transfer it to a view as a variable called ph.[0-9]
	#Also tells us that it can only be a number.
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name = 'post_detail'),
	url(r'^post/new/$', views.post_new, name = 'post_new'),
	url(r'^post/new/$', views.post_new, name = 'post_new'), 
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name = 'post_edit'),

]