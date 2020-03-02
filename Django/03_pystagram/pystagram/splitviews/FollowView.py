from .common import *

"""
[Pystagram] 팔로우 뷰
: 사용자가 팔로우 버튼이 클릭된 계정을 팔로우 할 수 있는 뷰
- FollowView is linked by follow_btn in post_list.html

1. 현재 사용자와 팔로우 대상 계정의 아이디를 이용해 following 테이블에 INSERT
2. post_list.html의 팔로우 수, 팔로우 버튼 → 언팔로우 버튼으로 변경 등을 위해
   포스트 리스트 페이지로 redirect
"""

@login_required
def FollowView(request, following_id):
    user = request.user

    try:
        cursor = connection.cursor()

        strSql = "INSERT INTO following(user_id, following_id)"
        strSql += " VALUES(%s, %s)"
        result = cursor.execute(strSql, (user.username, following_id))

        return redirect('pystagram:pn_post_list', following_id)

    except:
        connection.rollback()
        print("Failed inserting in FollowView")

        messages.error(request, "팔로우를 하는 과정에서 에러가 발생했습니다.")
        return redirect('pystagram:pn_post_list', following_id)

    finally:
        connection.close()