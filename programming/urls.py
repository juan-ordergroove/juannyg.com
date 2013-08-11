from django.conf.urls.defaults import *

from programming.views import index 

urlpatterns = patterns('',
  (r'^programming$', index),
)
