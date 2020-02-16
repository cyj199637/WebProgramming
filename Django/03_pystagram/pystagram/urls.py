from django.urls import re_path
from .splitviews import *

app_name = 'pystagram'

urlpatterns = [
    re_path(r'^$', MainView, name='pn_main'),
    re_path(r'^(?P<user_id>[a-zA-Z0-9-_.]*)/$', PostListView, name='pn_post_list'),
]