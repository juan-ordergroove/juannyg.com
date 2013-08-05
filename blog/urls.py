from django.conf.urls.defaults import *

from blog.views import index
from blog.views import blog_page

urlpatterns = patterns('',
  (r'^$', index),
  (r'^blog/page/(?P<page>\d+)$', blog_page),
)
