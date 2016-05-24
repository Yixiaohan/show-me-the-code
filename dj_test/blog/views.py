# -*- coding:utf-8 -*-
from django.shortcuts import render
from .models import Article, Category


CATEGORY = (u'行云流水', u'程序人生', u'痴人说梦')


# Create your views here.
def get_category():
    category_lists = Category.objects.all()
    category_lists = [category_list.__unicode__() for category_list in category_lists]
    return category_lists


def get_recent_lists():
    recent_lists = Article.objects.all().order_by('-create_at')[0:5]
    recent_lists = [recent_list.data for recent_list in recent_lists]

    return recent_lists


def home(request):
    article_lists = Article.objects.all().order_by('-create_at')
    article_lists = [article_list.data for article_list in article_lists]

    recent_lists = get_recent_lists()

    data = {
        'article_lists': article_lists,
        'recent_lists': recent_lists,
        'category_lists': get_category(),
    }
    return render(request, 'home.html', data)


def blog(request):
    article_lists = Article.objects.all().order_by('-create_at')
    article_lists = [article_list.data for article_list in article_lists]

    data = {
        'article_lists': article_lists,
    }
    return render(request, 'blog.html', data)


def article(request, pk):
    article = Article.objects.get(pk=pk).data
    recent_lists = get_recent_lists()

    data = {
        'article': article,
        'recent_lists': recent_lists,
        'category_lists': get_category(),
    }
    return render(request, 'article.html', data)


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def test(request):
    message = ['this a message']
    data = {
        'messages': message,
    }
    return render(request, 'test.html', data)