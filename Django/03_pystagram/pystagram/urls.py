from django.urls import re_path
from .splitviews import *

app_name = 'pystagram'

urlpatterns = [
    re_path(r'^$', PreMainView, name='pn_main'),
    # 나의 포스트 리스트 페이지 만들때 재활용
    # re_path(r'^(?P<user_id>[a-zA-Z0-9-_.]*)/$', PreMainView, name='pn_main'),
]