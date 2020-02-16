from django.urls import re_path
from .splitviews import *

app_name = 'accounts'

urlpatterns = [
    re_path(r'^register/$', RegisterAccountsView, name='pn_reg_accounts'),
    re_path(r'^login/$', LoginView, name='pn_login'),
    re_path(r'^logout/$', LogoutView, name='pn_logout'),
]