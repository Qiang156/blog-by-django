from django.shortcuts import render
from blog.models import Post

def index(request):
    posts = Post.objects.all()
    context = { "posts" : posts }
    return render(request, "blog/index.html", context)

def post_list(request):
    list_of_posts = Post.objects.order_by("created_at")
    context = { "posts" : list_of_posts }
    return render(request, 'blog/post_list.html', context)
    
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})