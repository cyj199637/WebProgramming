from .common import *

"""
[Pystagram] 포스트 수정 페이지
: 사용자가 포스트를 수정하는 페이지
- PostModifyView is linked by post_modify.html

1. request.method == GET
: post_modify.html rendering

2. request.method == POST
: post_modify.html 의 form 데이터를 받아와 post 테이블에 사용자가 선택한 포스트를 UPDATE
2.1 post_modify.html 의 form 데이터를 받아온다.
2.2 parameter로 받은 post_id를 조건하여 post 테이블에서 데이터 UPDATE
"""

@login_required
def PostModifyView(request, post_id):
    render_page = 'post_modify.html'
    if request.method == "GET":
        try:
            cursor = connection.cursor()

            strSql = "SELECT post_id, user_id, post_img_url, content, time"
            strSql += " FROM post"
            strSql += " WHERE post_id = (%s)"
            result = cursor.execute(strSql, (post_id,))
            datas = cursor.fetchall()

            post = {'post_id': datas[0][0],
                    'user_id': datas[0][1],
                    'post_img_url': datas[0][2],
                    'content': datas[0][3],
                    'time': datas[0][4]}

            return render(request, render_page, {'post': post,})

        except:
            connection.rollback()
            print("Failed selecting in PostModifyView")

            messages.error(request, "기존 포스트 정보를 불러오는데 에러가 발생했습니다.")
            return render(request, render_page)

        finally:
            connection.close()

    else:
        modifiedContent = request.POST.get('content')

        try:
            cursor = connection.cursor()

            strSql = "UPDATE post"
            strSql += " SET content = (%s)"
            strSql += " WHERE post_id = (%s)"
            result = cursor.execute(strSql, (modifiedContent, post_id))

            return redirect('pystagram:pn_post_detail', post_id)

        except:
            connection.rollback()
            print("Failed updating in PostModifyView")

            messages.error(request, "포스트를 수정하는데 에러가 발생했습니다.")
            return redirect('pystagram:pn_post_modify', post_id)

        finally:
            connection.close()