# -*- coding:utf-8 -*-

from django.contrib import admin
from models import MessageBoard
# Register your models here.

class MessageBoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'create_at')
    search_fields = ('name', 'message')

admin.site.register(MessageBoard, MessageBoardAdmin)
