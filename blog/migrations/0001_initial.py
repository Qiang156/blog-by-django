# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-10-22 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('sort', models.IntegerField(default=0, verbose_name='sort')),
            ],
            options={
                'db_table': 'blog_categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Content')),
                ('status', models.SmallIntegerField(choices=[(0, 'draft'), (1, 'published'), (2, 'deleted')], verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
            ],
            options={
                'db_table': 'blog_posts',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='User Name')),
                ('password', models.CharField(max_length=32, verbose_name='Password')),
                ('real_name', models.CharField(max_length=30, unique=True, verbose_name='Real Name')),
                ('gender', models.SmallIntegerField(choices=[(0, 'None'), (1, 'Male'), (2, 'Female')], verbose_name='Gender')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('last_login', models.DateTimeField(verbose_name='Last login')),
            ],
            options={
                'db_table': 'blog_users',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
    ]
