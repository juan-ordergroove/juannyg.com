from django.conf.urls.defaults import *

from me.views import index 

urlpatterns = patterns('',
  (r'^me$', index),
)
