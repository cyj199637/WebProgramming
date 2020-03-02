from .common import *

"""
[Pystagram] 포스트 업로드 페이지
: 사용자가 포스트를 업로드하는 페이지
- PostUploadView is linked by post_create.html

1. request.method == GET
: post_create.html rendering

2. request.method == POST
: post_create.html 의 form 데이터를 받아와 post 테이블에 데이터 INSERT
2.1 post_create.html 의 form 데이터를 받아온다.
2.2 post_img_url = fileUpload(user, postImg)
    - 사용자가 올린 사진 파일을 media 폴더에 저장한 후 저장된 경로를 return
2.3 post 테이블에 데이터 INSERT
"""

@login_required
def PostUploadView(request):
    user = request.user

    if request.method == 'GET':
        render_page = 'post_create.html'
        return render(request, render_page)

    else:
        content = request.POST.get('content')
        postImg = request.FILES.get('postImg')

        post_img_url = fileUpload(user, postImg)

        try:
            cursor = connection.cursor()

            strSql = "INSERT INTO post(user_id, post_img_url, content)"
            strSql += " VALUES(%s, %s, %s)"
            result = cursor.execute(strSql, (user.username, post_img_url, content))

            return redirect('pystagram:pn_main')

        except:
            connection.rollback()
            print("Failed inserting in PostUploadView")

            messages.error(request, "포스트를 업로드하는 과정에서 에러가 발생했습니다. 다시 시도해주세요.")
            return redirect('pystagram:pn_post_upload')

        finally:
            connection.close()