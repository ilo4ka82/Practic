from django.contrib import admin
from .models import Vacancy

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'posted_date')
    search_fields = ('title', 'company')

# Зарегистрируйте другие модели, если они есть
from .models import JobFormat, Skill

@admin.register(JobFormat)
class JobFormatAdmin(admin.ModelAdmin):
    pass

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

