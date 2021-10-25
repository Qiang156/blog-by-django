from django.shortcuts import render, get_object_or_404
from blog.models import Post,User

def index(request):
    posts = Post.objects.all()
    context = { "posts" : posts }
    return render(request, "blog/index.html", context)

def post_list(request):
    list_of_posts = Post.objects.order_by("created_at")
    context = { "posts" : list_of_posts }
    return render(request, 'blog/post_list.html', context)
    
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/detail.html', {'post': post})

def user_show(request, id):    
    post = get_object_or_404(User, pk=id)
    return render(request, 'blog/user.html', {'post': post})

