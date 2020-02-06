from .common import *

"""
[Pystagram] 메인 페이지
: 사용자의 포스트, 사용자가 팔로우한 계정의 포스트를 볼 수 있는 페이지
- MainView is linked by main.html
"""

@login_required
def MainView(request, user_id):
    render_page = "main.html"
    return render(request, render_page)