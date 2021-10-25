from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import UserLoginForm, UserRegisterForm

##for login/logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    context = { "just_testing" : "Hello!" }
    return render(request, "blog/index.html", context)

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