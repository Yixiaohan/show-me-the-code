# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MessageBoard(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default='anonymous')
    message = models.TextField(max_length=200, null=False, blank=False)
    create_at = models.TimeField(auto_created=True, auto_now_add=True)

    class Meta:
        verbose_name = 'message board'

    def __unicode__(self):
        return str(self.pk)
