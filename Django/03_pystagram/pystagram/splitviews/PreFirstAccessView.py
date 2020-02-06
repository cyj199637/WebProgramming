from .common import *

"""
[Pystagram] 사용자가 처음 접속할 때
: 사용자가 처음 접속할 때 동작하는 뷰

1. 세션에 로그인한 사용자의 user_id가 있는 경우
: 메인페이지로 redirect

2. 세션에 로그인한 사용자의 user_id가 없는 경우
: 로그인 페이지로 redirect
"""

def PreFirstAccessView(request):
    isSession = request.session.get('user_id', False)

    if isSession is not False:
        return redirect('pystagram:pn_main', isSession)

    else:
        return redirect('accounts:pn_login')