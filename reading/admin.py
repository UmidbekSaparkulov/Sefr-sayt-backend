from django.contrib import admin
from .models import ReadingTest, Option, Question, Segment, Paragraph, Heading


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class SegmentInline(admin.TabularInline):
    model = Segment
    extra = 1


class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 1


class HeadingInline(admin.TabularInline):
    model = Heading
    extra = 1


@admin.register(ReadingTest)
class ReadingTestAdmin(admin.ModelAdmin):
    list_display = ("title", "level", "type", "language")
    list_filter = ("level", "type", "language")
    search_fields = ("title",)
    inlines = [OptionInline, QuestionInline, SegmentInline, ParagraphInline, HeadingInline]
