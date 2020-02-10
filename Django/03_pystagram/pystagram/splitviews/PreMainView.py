from .common import *

"""
[Pystagram] 메인 페이지
: 사용자의 포스트, 사용자가 팔로우한 계정의 포스트를 볼 수 있는 페이지
- PreMainView is linked by main.html
"""

def PreMainView(request, user_id):
    isSession = request.session.get('user_id', False)

    if isSession is not False:
        render_page = "main.html"
        return render(request, render_page)

    else:
        return redirect('accounts:pn_login')