from django.contrib import admin
from .models import Todolist
# Register your models here.


class TodolistAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'todo')
    search_fields = ('user_name', 'todo')

admin.site.register(Todolist, TodolistAdmin)