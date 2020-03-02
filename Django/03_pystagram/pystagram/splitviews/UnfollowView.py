from .common import *

"""
[Pystagram] 언팔로우 뷰
: 사용자가 언팔로우 버튼이 클릭된 계정을 언팔로우 할 수 있는 뷰
- UnfollowView is linked by unfollow_btn in post_list.html

1. 현재 사용자와 언팔로우 대상 계정의 아이디를 이용해 following 테이블에서 DELETE
2. post_list.html의 팔로우 수, 언팔로우 버튼 → 팔로우 버튼으로 변경 등을 위해
   포스트 리스트 페이지로 redirect
"""

@login_required
def UnfollowView(request, following_id):
    user = request.user

    try:
        cursor = connection.cursor()

        strSql = "DELETE FROM following"
        strSql += " WHERE user_id = (%s)"
        strSql += " AND following_id = (%s)"
        result = cursor.execute(strSql, (user.username, following_id))

        return redirect('pystagram:pn_post_list', following_id)

    except:
        connection.rollback()
        print("Failed inserting in FollowView")

        messages.error(request, "언팔로우를 하는 과정에서 에러가 발생했습니다.")
        return redirect('pystagram:pn_post_list', following_id)

    finally:
        connection.close()