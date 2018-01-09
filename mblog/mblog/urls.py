"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from cblog.feeds import AllPostsRssFeed
from users import views
from django.views.generic.base import RedirectView

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'', include('cblog.urls')),
	url(r'', include('comments.urls')),
	# 记得在顶部引入 AllPostsRssFeed
	url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
	url(r'^search/', include('haystack.urls')),
	url(r'^users/', include('users.urls')),
	url(r'^users/',include('django.contrib.auth.urls')),
	# url(r'^index1/$', views.index1, name='index1')
	# any(r'^grappelli/',include('grappelli.urls')),
	# url(r'^check_is_login$', 'user_ex.views.check_is_login', name='check_is_login'),
	# url(r'^user_logout$', 'user_ex.views.user_logout', name='user_logout'),
	# url(r'^user_login$', 'user_ex.views.user_login', name='user_login'),
	# (r'^favicon.ico$','django.views.generic.simple.redirect_to’,{'url':'/static/images/favicon.ico}),
]
