from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from blog.models import Post, User
from blog.forms import PostForm

def index(request):
    context = { "just_testing" : "Hello!" }
    return render(request, "blog/index.html", context)

# To do: Later, when user can log in, we should add decorator @login_required
def edit_post(request, pk=0):
    # Same function for adding new blog post and editing existing blog post
    # And yes, maybe the code can be more efficient or shorter,
    # but the structure used is to make it clearer for human readers

    # NB! This line should be changed later, to get the real logged in user
    logged_in_user = User.objects.get(id=1)

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
                post_form_action = reverse("edit_post") + "0"
            elif request.method == "POST":
                # Save form data entered by user
                post_form = PostForm(request.POST)
                if post_form.is_valid():
                    post = post_form.save(commit=False)
                    post.author = logged_in_user
                    post.save()
                    return HttpResponseRedirect(reverse("edit_post") + str(post.id))
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
                    post_form_action = reverse("edit_post") + str(pk)
                elif request.method == "POST":
                    # Save form data edited by user
                    post_form = PostForm(request.POST, instance=post)
                    if post_form.is_valid():
                        post = post_form.save(commit=True)
                        return HttpResponseRedirect(reverse("edit_post") + str(pk))
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
