from .common import *

"""
[Pystagram] 사용자가 처음 접속할 때
: 사용자가 처음 접속할 때 동작하는 뷰

1. 세션에 로그인한 사용자의 user_id가 있는 경우
: 메인페이지로 redirect

2. 세션에 로그인한 사용자의 user_id가 없는 경우
: 로그인 페이지로 redirect
"""

def FirstAccessView(request):
    if not request.user.is_authenticated:
        return redirect('accounts:pn_login')
    else:
        user_id = request.user.username
        return redirect('pystagram:pn_main', user_id)