# -*- coding:utf-8 -*-
from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, help_text=u'类别名称')
    # alias = models.CharField(max_length=255, null=False, blank=False, help_text=u'英文别名')  # 链接用
    create_at = models.DateTimeField('create time', auto_now_add=True, null=False)
    update_at = models.DateTimeField('update time', auto_now=True)

    class Meta:
        verbose_name = 'category'

    def __unicode__(self):
        return self.name

    @property
    def data(self):
        return {
            'name': self.name,
            # 'alias': self.alias
        }


class Article(models.Model):

    title = models.CharField('title', null=False, blank=False, max_length=50, help_text=u'文章题目')
    author = models.CharField(max_length=255, default=u'wswang', null=False, blank=False, help_text=u'文章作者')

    create_at = models.DateTimeField('create time', auto_now_add=True, null=False)
    update_at = models.DateTimeField('update time', auto_now=True)

    abstract = models.CharField(max_length=255, null=False, blank=False, help_text=u'文章摘要')
    content = models.TextField('content', null=False, blank=False, help_text='content')

    tags = models.CharField('tags', null=True, max_length=30, help_text='tags')
    category = models.ForeignKey(Category, help_text=u'分类')

    def __unicode__(self):
        return self.title

    @property
    def data(self):
        return {
            'title': self.title,
            'pk': self.pk,
            'abstract': self.abstract,
            'category': self.category,
            'content': self.content,
            'create_at': self.create_at,
            'tags': self.tags,
        }
