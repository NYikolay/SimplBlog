from django.contrib import admin
from .models import *


class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']
    extra = 1


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at', 'is_published']
    list_filter = ['category', 'created_at', 'is_published']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'slug']
    list_display = ['title', 'slug']
    list_filter = ['title']
    prepopulated_fields = {'slug': ('title', )}


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ['post', 'name', 'email', 'created_at']
    list_filter = ['created_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)

