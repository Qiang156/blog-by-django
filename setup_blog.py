import os
import sys
import json
import sqlite3
import random


from blog_project.settings import DATABASES



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
    from django.conf import settings

    # -------------------------------------------------------------
    # delete all data exist
    # sqlite_sequence just for SQLite
    # -------------------------------------------------------------
    if settings.DATABASES['default']['ENGINE'].index('sqlite3'):
        con= sqlite3.connect("./db.sqlite3")
        cursor = con.cursor()
        cursor.execute('DELETE FROM blog_categories')
        cursor.execute('DELETE FROM blog_users')
        cursor.execute('DELETE FROM blog_posts')
        cursor.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name="blog_users"')
        cursor.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name="blog_categories"')
        cursor.execute('UPDATE sqlite_sequence SET seq = 0 WHERE name="blog_posts"')
        con.commit()
        con.close()
    else:
        User.objects.all().delete();
        Category.objects.all().delete();
        Post.objects.all().delete();
    # -------------------------------------------------------------

    category_list = ['general','community','interviews','meta','security']

    userData = [{
        'name':'Johan', 'password':'88888888', 'real_name':'Johan',
        'gender':1, 'email':'Johan@gmail.com'
    },{
        'name':'Qiang', 'password':'88888888', 'real_name':'Qiang',
        'gender':1, 'email':'admin@gmail.com'
    },{
        'name':'Magdaleda', 'password':'88888888', 'real_name':'Magdaleda',
        'gender':1, 'email':'Magdaleda@gmail.com'
    },{
        'name':'Yali', 'password':'88888888', 'real_name':'Yali',
        'gender':1, 'email':'Yali@gmail.com'
    },{
        'name':'Raul', 'password':'88888888', 'real_name':'Raul',
        'gender':1, 'email':'Raul@gmail.com'
    }]
    userList = []
    for item in userData:
        userList.append(User.objects.create(**item))

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
                            author=userList[random.randint(0,4)],
                            status=1)
                post.save()

    print("populate was successful")

if __name__ == '__main__':
    main()
