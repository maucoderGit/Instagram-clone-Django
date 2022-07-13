"""Posts admin settings file"""
# Python
from typing import Optional
# Django
from django.contrib import admin
# models
from django.contrib.auth.models import User
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin class"""

    fieldsets: Optional[set] = (
        (
            'Post', {
                'fields': (('title', 'photo'),)
            }
        ),
        (
            'User info', {
                'fields': (
                    ('user'),
                    ('profile'),

                )
            }
        ),
        (
            'Metadata', {
                'fields': (('created', 'modified'),)
            }
        )
    )

    list_display = ('pk', 'title', 'photo', 'user')

    readonly_fields = ('created', 'modified')

    search_fields: list|tuple[str] = (
        'user__username',
        'title', 
        'pk',
    )
    list_filter: list|tuple[str] = (
        'created',
        'modified',
    )
