from .common import *

"""
[Pystagram] 나의 포스팅 페이지
: 사용자가 작성한 포스트만을 볼 수 있는 페이지
- PostListView is linked by post_list.html

1. 아이디가 클릭된 유저의 포스트 리스트를 SELECT
2. 가져온 포스트를 post_list.html에 rendering
"""

@login_required
def PostListView(request, user_id):
    user = request.user

    try:
        cursor = connection.cursor()

        strSql = "SELECT post_id, post_img_src"
        strSql += " FROM post"
        strSql += " WHERE user_id = (%s)"
        strSql += " ORDER BY time DESC"

        result = cursor.execute(strSql, (user_id,))
        datas = cursor.fetchall()

        posts = []
        for data in datas:
            raw_data = {'post_id': data[0],
                        'post_img_src': data[1],}
            posts.append(raw_data)

        render_page = "post_list.html"
        return render(request, render_page, {'user_id': user_id, 'posts': posts})


    except:
        connection.rollback()
        print("Failed selecting in MainView")

        messages.error(request, "포스트를 가져오는데 에러가 발생하였습니다.")
        render_page = "post_list.html"
        return render(request, render_page, {'user_id': user_id,})

    finally:
        connection.close()