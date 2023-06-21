from django.contrib import admin

from .models import News, Comments


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'likes', 'author', 'created')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'post_id', 'author_id', 'created')


admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)
