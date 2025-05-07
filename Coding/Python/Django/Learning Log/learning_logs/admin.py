from django.contrib import admin

from .models import Topic, Entry


# Admin Models
class TopicAdmin(admin.ModelAdmin):
    """
    Place Holder
    """
    list_display = ('text', 'date_added', 'owner')


# Register your models here.
admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry)
