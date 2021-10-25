from django.shortcuts import render, get_object_or_404
from blog.models import Post,User,Category

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
    
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/detail.html', {'post': post})

def user_show(request, id):    
    post = get_object_or_404(User, pk=id)
    return render(request, 'blog/user.html', {'post': post})

#def index(request):
    #post_list = Post.objects.all().order_by('-created_at')
    #category_list = Category.objects.all()
    
    #return render(request, 'blog/index.html', context={'post_list': post_list, 'category_list': category_list})
   
def getPost(request, post_id):
    currentPost = Post.objects.get(id = post_id)
    return render(request, 'blog/viewPost.html', context={'post': currentPost})
