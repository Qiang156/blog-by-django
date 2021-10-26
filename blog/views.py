from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from blog.forms import PostForm, UserLoginForm, UserRegisterForm
from blog.models import Post, Category

##for login/logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def index(request,category=0,user=''):
    category_list = Category.objects.all()
    user_list = User.objects.filter(is_superuser=False).order_by('username')
    posts = Post.objects.all().order_by('-created_at')
    
    if category:
        category = Category.objects.filter(name=category)
        posts = posts.filter(category=category)
    if user:
        user = User.objects.filter(username=user)
        posts = posts.filter(author=user)
    
    context = { "posts" : posts, 'category_list': category_list,'user_list':user_list} 
    return render(request, "blog/index.html", context )

# To do: Later, when user can log in, we should add decorator @login_required
# Now == Later. Login functionality has been added 
@login_required
def edit_post(request, pk=0):
    # Same function for adding new blog post and editing existing blog post
    # And yes, maybe the code can be more efficient or shorter,
    # but the structure used is to make it clearer for human readers

    # NB! This line should be changed later, to get the real logged in user
    #logged_in_user = User.objects.get(id=1)
    # Now == Later. Get the real logged in user
    logged_in_user = request.user

    if pk == "":
        # The url was /blog/edit_post/, without any pk value
        # Show a list of this user's posts
        list_of_posts_by_user = Post.objects.filter(author=logged_in_user).order_by("-created_at")
        context = { "list_of_posts_by_user": list_of_posts_by_user }
    else:
        # Create or edit a single post
        if pk == "0":
            # The url was /blog/edit_post/0
            # We are about to add a new blog post
            if request.method == "GET":
                # Just show empty form for user to fill out
                post_form = PostForm()
                post_form_action = reverse("blog:edit_post") + "0"
            elif request.method == "POST":
                # Save form data entered by user
                post_form = PostForm(request.POST)
                if post_form.is_valid():
                    post = post_form.save(commit=False)
                    post.author = logged_in_user
                    post.save()
                    return HttpResponseRedirect(reverse("blog:edit_post") + str(post.id))
                else:
                    # Oops, some error, add handler later
                    pass
            else:
                # Some unknown method used, handle that later
                pass
        else:
            # The url was /blog/edit_post/[number], with a pk value
            # We are about to edit an existing blog post
            post = get_object_or_404(Post, pk=pk)
            if post.author == logged_in_user:
                if request.method == "GET":
                    # Just show form for user to edit
                    post_form = PostForm(instance=post)
                    post_form_action = reverse("blog:edit_post") + str(pk)
                elif request.method == "POST":
                    # Save form data edited by user
                    post_form = PostForm(request.POST, instance=post)
                    if post_form.is_valid():
                        post = post_form.save(commit=True)
                        return HttpResponseRedirect(reverse("blog:edit_post") + str(pk))
                    else:
                        # Oops, some error, add handler later
                        pass
                else:
                    # Some unknown method used, handle that later
                    pass
            else:
                # Someone trying to edit another user's post
                raise PermissionDenied()
        context = { "post_form": post_form, "post_form_action": post_form_action }

    # Finally, render the page using template edit_post.html
    return render(request, "blog/edit_post.html", context)
 
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

def getPost(request, post_id):
    currentPost = Post.objects.get(id = post_id)
    return render(request, 'blog/viewPost.html', context={'post': currentPost})
    
def user_login(request):
    error = False   ## flag errors
    message = ""
    context = {}

    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error = True
                message = 'Account not Active'
        else:
            error = True
            message = 'Login failed. Please verify your credentials'
    else:
        pass

    if error:
        context = {'error': error, 'message' : message}
        
    return render(request, 'blog/login.html', context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    username = ''

    if request.method == "POST":
        user_form = UserRegisterForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            username = user.username
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserRegisterForm()        

    context = {'user_form': user_form, 'username' : username, 'registered': registered}

    return render(request, 'blog/register.html', context)
