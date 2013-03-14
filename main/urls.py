from django.conf.urls.defaults import *

from main.views import index

urlpatterns = patterns('',
  (r'^', index)
)
