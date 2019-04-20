from django.contrib import admin

from .models import Question, Video, Choice


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    list_filter = ['title']


# admin.site.register(Video, VideoAdmin)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    show_change_link = True


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
