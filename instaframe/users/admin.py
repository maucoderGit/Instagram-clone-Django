"""Admin settings file"""
# Python
from typing import Optional, Sequence
# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
# models
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin class"""
    fieldsets: dict[tuple] = (
        ('Profile', {
            'fields': tuple(('user', 'picture'))
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': tuple(('created', 'modified'))
        })
    )
    readonly_fields = ('created', 'modified', 'user')
    
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user', 'picture')
    list_editable: Sequence[str] = (
   
    )
    search_fields: Sequence[str] = (
        'user__email',
        'user__first_name',
        'user__last_name', 
        'user__pk',
        'user__username'
    )
    list_filter: list|tuple[str] = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',
    )


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users"""
    model = Profile
    can_delete = False
    verbose_name_plural: Optional[str] = 'profiles'


class UserAdmin(BaseUserAdmin):
    """add profile admin to base user admin"""
    inlines = (ProfileInline,)
    list_display: tuple = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)