from django.urls import re_path
from .splitviews import *

app_name = 'pystagram'

urlpatterns = [
    re_path(r'^$', PreFirstAccessView, name='pn_first_access'),
    re_path(r'^(?P<user_id>[a-zA-Z0-9-_.]*)/$', PreMainView, name='pn_main'),
]