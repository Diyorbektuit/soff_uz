from django.contrib import admin
from .models import Test, Question
# Register your models here.


class TestAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'height_score')


admin.site.register(Test, TestAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'question')


admin.site.register(Question, QuestionAdmin)
