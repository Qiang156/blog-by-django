from django.shortcuts import render
from blog.models import Category, Post


def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    category_list = Category.objects.all()
    
    return render(request, 'blog/index.html', context={'post_list': post_list, 'category_list': category_list})
   
def getPost(request, post_id):
    currentPost = Post.objects.get(id = post_id)
    return render(request, 'blog/viewPost.html', context={'post': currentPost})
