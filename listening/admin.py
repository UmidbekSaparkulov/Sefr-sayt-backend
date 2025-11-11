from django.contrib import admin
from .models import ListeningTest, ListeningQuestion, ListeningOption


class ListeningOptionInline(admin.TabularInline):
    model = ListeningOption
    extra = 2


class ListeningQuestionInline(admin.TabularInline):
    model = ListeningQuestion
    extra = 1


@admin.register(ListeningTest)
class ListeningTestAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "type", "language")
    list_filter = ("level", "type", "language")
    search_fields = ("title",)
    inlines = [ListeningQuestionInline]
