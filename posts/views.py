from django.shortcuts import render, redirect
from .models import Post, Like
from profiles.models import Profile
from .forms import PostModelForm, CommentModelForm


# Create your views here.


def post_comment_create_and_list_view(request):
    query_set = Post.objects.all()
    profile = Profile.objects.get(user=request.user)

    # creating post and comment form
    post_form = PostModelForm()
    comment_form = CommentModelForm()
    post_added = False

    # profile = Profile.objects.get(user=request.user)
    if 'submit_post_form' in request.POST:
        post_form = PostModelForm(request.POST, request.FILES)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.author = profile
            instance.save()
            post_form = PostModelForm()
            post_added = True

    if 'submit_comment_form' in request.POST:
        comment_form = CommentModelForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            comment_form = CommentModelForm()

    context = {
        'query_set': query_set,
        'profile': profile,
        'post_form': post_form,
        'comment_form': comment_form,
        'post_added': post_added,
    }
    return render(request, 'posts/main.html', context)


def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'

        post_obj.save()
        like.save()

    return redirect('posts:main_post_view')
