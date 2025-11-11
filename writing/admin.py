from django.contrib import admin
from .models import Writing

@admin.register(Writing)
class WritingAdmin(admin.ModelAdmin):
    list_display = ('part', 'topic', 'question', 'created_at')
    search_fields = ('part', 'topic', 'question')
