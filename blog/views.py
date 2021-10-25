from django.shortcuts import render
from blog.models import Post

def index(request):
    posts = Post.objects.all()
    post_list = Post.objects.all().order_by('-created_at')
    category_list = Category.objects.all()
    context = { "posts" : posts ,'post_list1': post_list, 'category_list': category_list} 

    return render(request, "blog/index.html", context )
 
def post_list(request):
    list_of_posts = Post.objects.order_by("created_at")
    context = { "posts" : list_of_posts }
    return render(request, 'blog/post_list.html', context)
    
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
from blog.models import Category, Post


#def index(request):
    #post_list = Post.objects.all().order_by('-created_at')
    #category_list = Category.objects.all()
    
    #return render(request, 'blog/index.html', context={'post_list': post_list, 'category_list': category_list})
   
def getPost(request, post_id):
    currentPost = Post.objects.get(id = post_id)
    return render(request, 'blog/viewPost.html', context={'post': currentPost})
