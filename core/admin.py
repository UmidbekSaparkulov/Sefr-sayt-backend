from django.contrib import admin
from .models import Level, Skill


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)
