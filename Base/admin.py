from django.contrib import admin
from .models import Category, BlogPost, Tag


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published')
    list_filter = ('author__username', 'published')
    ordering = ['-created_at']

admin.site.register(BlogPost, BlogPostAdmin)

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)