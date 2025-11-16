from django.contrib import admin
from .models import Writing

@admin.register(Writing)
class WritingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "type", "get_themes")
    search_fields = ("title", "type", "description")
    list_filter = ("type",)

    def get_themes(self, obj):
        return ", ".join(obj.themes)
    get_themes.short_description = "Themes"
