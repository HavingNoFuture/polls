from django.contrib import admin
from .models import Poll, Question


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


