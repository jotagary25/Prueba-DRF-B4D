from typing import Any
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'modified_at', 'view_post_link']
    fields = ['title', 'content']
    exclude = ['author']
    readonly_fields = ['author']

    def view_post_link(self, obj):
        url = reverse('post-detail', args=[obj.pk])
        return format_html('<a href="{}">View post</a>', url)
    
    view_post_link.short_description = 'Post Link'

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)