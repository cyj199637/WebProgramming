from .common import *

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