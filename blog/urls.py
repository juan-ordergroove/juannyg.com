from django.conf.urls.defaults import *

from blog.views import index
from blog.views import blog_page
from blog.views import blog_archive

urlpatterns = patterns('',
  (r'^$', index),
  (r'^blog/page/(?P<page>\d+)$', blog_page),
  (r'^blog/(?P<year>\d{4})/(?P<month>\d{2})$', blog_archive),
)
