import os
import sys
import json


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
    try:
        import django
        django.setup()
    except ImportError as exe:
        raise BaseException(exe.msg)

    # from django.db import transaction
        
    from blog.models import User, Category, Post

    """"
    delete all data exist
    """
    User.objects.all().delete()
    Category.objects.all().delete()
    Post.objects.all().delete()

    category_list = ['general','community','interviews','meta','security']

    userdata = {
        'name':'admin', 'password':'88888888', 'real_name':'Administrator',
        'gender':1, 'email':'admin@gmail.com'
    }
    user = User.objects.create(**userdata)
    key = 0
    for value in category_list:
        key = key + 1
        tmp = { 'name':value, 'sort': key }
        category = Category.objects.create(**tmp)
        
        with open("./data/"+value+".json",'r') as f:
            for post in json.load(f):
                post = Post(title=post['title'],
                            body=post['content'],
                            category=category,
                            author=user,
                            status=1)
                post.save()

    print("populate was successful")

if __name__ == '__main__':
    main()
