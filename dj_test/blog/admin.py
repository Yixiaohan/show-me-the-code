from django.contrib import admin
from models import Article, Author

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'age', 'status', 'sex')
    search_fields = ('author', )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pk', 'tags')
    search_fields = ('title', 'tags')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)