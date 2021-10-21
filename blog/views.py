from django.shortcuts import render

def index(request):
    context = { "just_testing" : "Hello!" }
    return render(request, "blog/index.html", context)

