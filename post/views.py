from django.shortcuts import render, HttpResponse, get_object_or_404

from post.models import Post


def post_index(request):
    context = Post.objects.all()
    return render(request,'post/index.html',{'posts': context} )


def post_detail(request,id):
    context = get_object_or_404(Post,id=id)
    return render(request, 'post/detail.html', {'posts': context})


def post_update(request):
    return HttpResponse('post_update')


def post_delete(request):
    return HttpResponse('post_delete')


def post_create(request):
    return HttpResponse('post_create')