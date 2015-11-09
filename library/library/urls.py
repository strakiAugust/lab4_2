"""library URL Configuration

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
#from django.conf.urls import include, url
from django.conf.urls import *
from django.contrib import admin
#from library.books import views
from books.views import *
from contact.views import *

#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#]

urlpatterns = patterns('',
    (r'^$', index),
    (r'^admin/', include(admin.site.urls)),
#    (r'^search_form/$', search_form),
    (r'^search/$', search),
    (r'^contact/$', contact),
    (r'^addbook/$', addbook),
    (r'^booklist/$', booklist),
    (r'^information/$', information),
    (r'^addauthor/$', addauthor),
    (r'^authorlist/$', authorlist),
    (r'^deletebook/$', booklist),
    (r'^deleteauthor/$', authorlist),
    (r'^updatebook/$', updatebook),
    (r'^updatebookform/$', updatebookform),

)