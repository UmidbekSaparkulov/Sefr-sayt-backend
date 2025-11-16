from django.contrib import admin
from .models import ListeningTest, ListeningQuestion, ListeningOption

class ListeningOptionInline(admin.TabularInline):
    model = ListeningOption
    extra = 0

class ListeningQuestionInline(admin.TabularInline):
    model = ListeningQuestion
    extra = 0
    inlines = [ListeningOptionInline]

@admin.register(ListeningTest)
class ListeningTestAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "skill", "type")
    inlines = [ListeningQuestionInline]

@admin.register(ListeningQuestion)
class ListeningQuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "listening_test", "order", "correct_answer")

@admin.register(ListeningOption)
class ListeningOptionAdmin(admin.ModelAdmin):
    list_display = ("question", "key", "text", "is_correct")
