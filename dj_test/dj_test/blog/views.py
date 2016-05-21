# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.

def home_page(request):
    blog_name = "myblog"
    article_lists = Article.objects.all().order_by('-create_at')
    article_lists = [article_list.data for article_list in article_lists]

    data = {
        'blog_name': blog_name,
        'article_lists': article_lists,
    }
    return render(request, 'home_page.html', data)


def article_view(request, pk):
    # title = request.GET.get('title', '')
    # title = u'这里是文章的题目'   # test

    article = get_object_or_404(Article, pk=pk).data

    return render(request, 'article.html', article)

def test(request):
    message = ['this a message']
    data = {
        'messages': message,
    }
    return render(request, 'test.html', data)