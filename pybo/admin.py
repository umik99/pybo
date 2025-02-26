from django.contrib import admin
from .models import Question, Answer

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Answer)
admin.site.register(Question,QuestionAdmin)