from django.contrib import admin
from .models import *


# Register your models here.

class Educational_InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'address',)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',  'email',  'year_of_graduation', 'educational_institution', 'level_of_education',
        'use_result', 'gpa', 'is_staff',)
    list_display_links = ('id',  'email', )
    search_fields = ('id',   'email',)
    list_filter = ('is_staff', 'level_of_education', 'year_of_graduation',)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'document_type', 'date_add',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'user__username',)
    list_filter = ('document_type',)


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'period_of_study', 'price', 'year', 'level_of_education',)
    list_display_links = ('id', 'name',)
    list_filter = ('year', 'level_of_education', 'period_of_study',)
    search_fields = ('name',)


class List_QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'user', 'date',)
    search_fields = ('question__text', 'user__username',)


class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'position',)
    list_filter = ('position',)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profession', 'specialist', 'status', 'date', 'date_of_appointment',)
    search_fields = ('user__username', 'profession__name',)
    list_filter = ('status', 'date', 'date_of_appointment', 'profession__name',)
    list_editable = ('status', 'date_of_appointment',)


admin.site.register(Educational_Institution, Educational_InstitutionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(List_Questions, List_QuestionsAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Application, ApplicationAdmin)
