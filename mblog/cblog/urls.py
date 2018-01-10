from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.contrib import admin

from . import views

app_name = 'cblog'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
	url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
	url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_article/$', views.add_article, name='add_article'),
	url(r'^edit/(?P<pk>[0-9]+)/$', views.edit, name='edit'),
	url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
	# url(r'^admins/', admin.site.urls),
	# url(r'^search/$', views.search, name='search'),
	# url(r'^login/$',views.login,name='login'),
]
