from django.contrib import admin
from .models import TestInfo, TestTip, Expectation, SampleQuestion, SampleQuestionGuideline

# TestInfo
@admin.register(TestInfo)
class TestInfoAdmin(admin.ModelAdmin):
    list_display = ("questions", "minutes", "task_types")
    search_fields = ("questions", "minutes", "task_types")

# TestTip
@admin.register(TestTip)
class TestTipAdmin(admin.ModelAdmin):
    list_display = ("text",)
    search_fields = ("text",)

# Expectation
@admin.register(Expectation)
class ExpectationAdmin(admin.ModelAdmin):
    list_display = ("text",)
    search_fields = ("text",)

# SampleQuestionGuideline (Inline sifatida)
class SampleQuestionGuidelineInline(admin.TabularInline):
    model = SampleQuestionGuideline
    extra = 1

# SampleQuestion
@admin.register(SampleQuestion)
class SampleQuestionAdmin(admin.ModelAdmin):
    list_display = ("task_title", "image_url", "preparation", "speaking")
    search_fields = ("task_title", "prompt")
    inlines = [SampleQuestionGuidelineInline]
