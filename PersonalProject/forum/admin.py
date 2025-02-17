from django.contrib import admin
from .models import Category, Thread, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')


class PostAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_by', 'created_at', 'thread')
    list_filter = ('thread',)
    search_fields = ('content', 'created_by')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
