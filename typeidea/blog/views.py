from django.http import HttpResponse


def post_list(request, category_id=None, tag_id=None):
    content = 'post_list category_id={category_id}, tag_id={tag_id}'.format(
        category_id=category_id,
        tag_id=tag_id,
    )

    return HttpResponse(content)


def post_detail(request, post_id):
    return HttpResponse('detail')
