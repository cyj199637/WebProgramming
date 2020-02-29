from .common import *

@login_required
def PostModifyView(request, post_id):
    if request.method == "GET":
        render_page = 'post_modify.html'
        return render(request, render_page)

    else:
        pass