# -*- coding:utf-8 -*-
from django.db import models
# Create your models here.


class Author(models.Model):
    MALE = 1
    FEMALE = 0
    SEX_CHOICE = ((MALE, u'male'), (FEMALE, u'female'))

    author = models.CharField('author name', null=False, max_length=30, blank=False, unique=True,)
    sex = models.IntegerField('sex', choices=SEX_CHOICE, help_text="sex")
    age = models.IntegerField('age', null=True, default=0, help_text="age")
    status = models.BooleanField('status', default=True, help_text='user status')

    def __unicode__(self):
        return self.author

    # class Meta:
    #     abstract = True

    def user_data(self):
        return {
            'user_name': self.user_name,
            'sex': self.sex,
            'age': self.age,
        }


class Article(models.Model):
    TALKING = 0
    CODING = 1
    DREAMING = 2
    CATEGORY_CHOICE = ((TALKING, u'行云流水'), (CODING, u'程序人生'), (DREAMING, u'痴人说梦'))

    title = models.CharField('title', null=False, blank=False, max_length=50, help_text=u'文章题目')
    author = models.CharField(max_length=255, default=u'wswang', null=False, blank=False, help_text=u'文章作者')
    content = models.TextField('content', null=False, blank=False, help_text='content')
    create_at = models.DateTimeField('create time', auto_now_add=True, null=False)
    update_at = models.DateTimeField('update time', auto_now=True)
    tags = models.CharField('tags', null=True, max_length=30, help_text='tags')
    category = models.IntegerField(choices=CATEGORY_CHOICE, default=CODING, help_text=u'文章分类')

    def __unicode__(self):
        return self.title

    @property
    def data(self):
        return {
            'title': self.title,
            'pk': self.pk,
            'author': self.author,
            'category': self.category,
            'content': self.content,
            'create_at': self.create_at,
            'update_at': self.update_at,
            'tags': self.tags,
        }