from django.conf.urls.defaults import *

from about.views import index

urlpatterns = patterns('',
  (r'^about$', index),
)
