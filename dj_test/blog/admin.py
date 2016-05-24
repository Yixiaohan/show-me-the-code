# -*- coding:utf-8 -*-
from django.contrib import admin
from models import Article, Author, Category
from form import ArticleForm
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'age', 'status', 'sex')
    search_fields = ('author', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at')
    search_fields = ('name', )


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ('title', 'abstract', 'content', 'category', 'tags')
    search_fields = ('title', 'tags', 'abstract', 'content')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
