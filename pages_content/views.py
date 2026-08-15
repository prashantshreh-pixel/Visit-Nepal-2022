from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.


def post_view(request):
    if (request.method == 'GET'):
        id = int(request.GET["id"])
        pst = Post.objects.filter(id=id)
        comment = Comment.objects.all().filter(post=pst[0])

        context = {
            "data": pst,
            "content": comment,
        }
        return render(request, 'contentindex.html', context)
    else:
        id = int(request.GET["id"])
        pst = Post.objects.filter(id=id)
        desc_cmt = request.POST['comment']

        comment = Comment.objects.create(
            post=pst[0], user=request.user, cmt=desc_cmt)
        comment.save()
        return redirect("/post?id="+str(id))
