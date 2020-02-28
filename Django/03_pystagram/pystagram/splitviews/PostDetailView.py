from .common import *

"""
[Pystagram] 포스트 상세 페이지
: 사용자가 작성한 포스트만을 볼 수 있는 페이지
- PostDetailViewView is linked by post_detail.html

1. 클릭된 포스트를 SELECT
2. 가져온 포스트를 post_detail.html에 rendering
"""

def PostDetailView(request, post_id):
    user = request.user

    try:
        cursor = connection.cursor()

        strSql = "SELECT post_id, user_id, post_img_url, content, time"
        strSql += " FROM post"
        strSql += " WHERE post_id = (%s)"
        result = cursor.execute(strSql, (post_id,))
        data = cursor.fetchall()
        data = [list(x) for x in data]

        post = {'post_id': data[0][0],
                'user_id': data[0][1],
                'post_img_url': data[0][2],
                'content': data[0][3],
                'time': data[0][4]}

        postDetailUser = User.objects.get(username=post['user_id'])

        render_page = 'post_detail.html'
        return render(request, render_page, {'postDetailUser': postDetailUser, 'post': post})

    except:
        connection.rollback()
        print("Failed selecting in PostDetailView")

        messages.error(request, "포스트를 가져오는데 에러가 발생하였습니다.")
        render_page = 'post_detail.html'
        return render(request, render_page)

    finally:
        connection.close()