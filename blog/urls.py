from django.conf.urls.defaults import *

from blog.views import index, blog_page, blog_archive
from me.views import index as me_index

urlpatterns = patterns('',
  (r'^$', index),

  (r'^blog$', blog_archive),
  (r'^blog/(?P<id>[0-9a-f]{24})$', blog_archive),
  (r'^blog/page/(?P<page>\d+)$', blog_page),

  (r'^blog/(?P<year>\d{4})/(?P<month>\d{1,2})$', blog_archive),
  (r'^blog/(?P<year>\d{4})/(?P<month>\d{1,2})/page/(?P<page>\d+)$', blog_page),
)
