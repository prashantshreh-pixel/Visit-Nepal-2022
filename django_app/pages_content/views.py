from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post, Comment

# Create your views here.


def post_view(request):
    post_id = request.GET.get("id")
    
    # Graceful fallback if no id or invalid id is passed
    if not post_id:
        first_post = Post.objects.first()
        if first_post:
            return redirect(f"/post?id={first_post.id}")
        messages.info(request, "No posts available at the moment.")
        return redirect("explore")

    try:
        post = Post.objects.select_related('Category').get(pk=post_id)
    except (Post.DoesNotExist, ValueError):
        first_post = Post.objects.first()
        if first_post:
            return redirect(f"/post?id={first_post.id}")
        messages.error(request, "The requested post could not be found.")
        return redirect("explore")

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in to post a comment.')
            return redirect(f"/login/?next=/post%3Fid%3D{post.id}")

        desc_cmt = request.POST.get('comment', '').strip()
        parent_id = request.POST.get('parent_id')

        if desc_cmt:
            parent_comment = None
            if parent_id:
                try:
                    parent_comment = Comment.objects.get(pk=parent_id, post=post)
                except Comment.DoesNotExist:
                    parent_comment = None

            Comment.objects.create(
                post=post,
                user=request.user,
                cmt=desc_cmt,
                parent=parent_comment
            )
            messages.success(request, 'Comment posted successfully!')
        return redirect(f"/post?id={post.id}")

    # Fetch root comments with their replies pre-fetched
    root_comments = Comment.objects.filter(post=post, parent=None).select_related('user').prefetch_related(
        'replies', 'replies__user', 'replies__replies', 'replies__replies__user'
    ).order_by('-timestamp')

    total_comments_count = Comment.objects.filter(post=post).count()

    context = {
        "post": post,
        "comments": root_comments,
        "total_comments_count": total_comments_count,
    }
    return render(request, 'contentindex.html', context)
