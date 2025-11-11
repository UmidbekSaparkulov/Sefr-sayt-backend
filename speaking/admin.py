from django.contrib import admin
from .models import Speaking

@admin.register(Speaking)
class SpeakingAdmin(admin.ModelAdmin):
    list_display = ('part', 'topic', 'question', 'created_at')
    search_fields = ('part', 'topic', 'question')
