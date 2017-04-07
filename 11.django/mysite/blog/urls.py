# coding:utf-8
from django.conf.urls import patterns

# from blog.views import *

urlpatterns = patterns('blog.views', # 视图前缀
                       (r'^$', 'archive'), # 相当于 'blog.views.archive'
                       (r'^create/$', 'create_blogpost'),
                       )
# urlpatterns = patterns('blog.views',
#                        (r'^$', 'archive'))
# 等同于
# from django.conf.urls import url
# urlpatterns = patterns('blog.views',
#                        url(r'^$', 'archive'))
