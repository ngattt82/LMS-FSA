from django.contrib import admin
from .models import DiscussionThread  # Import your model

@admin.register(DiscussionThread)
class DiscussionThreadAdmin(admin.ModelAdmin):
    list_display = ('thread_title', 'created_by', 'created', 'updated')  # Customize as needed
    search_fields = ('thread_title','thread_content')
