from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.http import HttpResponse
from blog.forms import UserLoginForm, UserRegisterForm

##for login/logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

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
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('Login failed. Please verify your credentials')
            return HttpResponse('Invalid login')
    else:
        return render(request, 'blog/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserRegisterForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserRegisterForm()        

    return render(request, 'blog/register.html', {'user_form': user_form, 'registered': registered})
