from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Topic, Entry

# Unregister default User model
admin.site.unregister(User)


# Admin Models
class TopicAdmin(admin.ModelAdmin):
    """
    Custom display settings for the Topic model in the Django admin interface.
    """
    list_display = ('custom_title', 'date_added', 'owner')
    list_filter = ('owner', 'date_added')

    def custom_title(self, obj):
        """Returns  the 'text' field of the Topic model for display."""
        return obj.text

    # Enables sorting behavior for the 'Topics' column in the admin list view.
    custom_title.admin_order_field = 'text'
    # Changes the header text of the custom column to 'Topics'.
    custom_title.short_description = 'Topics'


class EntryAdmin(admin.ModelAdmin):
    """
    Custom display settings for the Entry model in the Django admin interface.
    """
    list_display = ('custom_title', 'date_added', 'owner')
    list_filter = ('owner', 'date_added')

    def custom_title(self, obj):
        """
        Returns the 'text' field of the Topic model for display, truncated
        to 50 characters then formats it with ellipsis if it's too long.
        """
        entry = obj.text
        return entry[:50] + ('...' if len(entry) > 50 else '')

    # Enables sorting behavior for the 'Entries' column in the admin list view.
    custom_title.admin_order_field = 'text'
    # Changes the header text of the custom column to 'Entries'.
    custom_title.short_description = 'Entries'


# Decorator to register custom UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom displa settings for the Users admin panel
    """
    list_display = (
        'username',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'last_login',
        )
    list_filter = (
        'username',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'last_login',
        )


# Register your models here.
admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)
