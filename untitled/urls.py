"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from registration import registr
from contact.views import contact
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', views.hello),
    url(r'^time/$', views.current_datetime, name='current_dt'),
    url(r'^time/plus/(?P<offset>\d{1,2})/$', views.hours_ahead),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact),
    url(r'^registration/$', registr.register),
    url(r'^login/$', registr.login),
    url(r'^logout/$', registr.logout),
    url(r'^blog/', include('blog.urls')),
    url(r'', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))



]

