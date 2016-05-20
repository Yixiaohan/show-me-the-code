# -*- coding:utf-8 -*-
from django.shortcuts import render
from .models import Article


# Create your views here.

def home_page(request):
    blog_name = "myblog"
    article_lists = Article.objects.all().order_by('-create_at')
    article_lists = [article_list.title for article_list in article_lists]

    data = {
        'blog_name': blog_name,
        'article_lists': article_lists,
    }
    return render(request, 'home_page.html', data)

def article_view(request):
    title = request.GET.get('title', '')
    title = u'这里是文章的题目'   # test

    article = Article.objects.get(title=title)
    title = article.title
    content = article.content
    create_at = article.create_at
    # author = article.author

    data = {
        'title': title,
        'author': 'wang',
        'content': content,
        'create_at': create_at,
    }

    return render(request, 'article.html', data)

def test(request):
    message = ['this a message']
    data = {
        'messages': message,
    }
    return render(request, 'test.html', data)