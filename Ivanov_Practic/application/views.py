import requests
from django.shortcuts import render
from django.db.models import Count
from .models import Vacancy, Skill, JobFormat
from .forms import ParseForm, VacancySearchForm
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("Welcome to the Job Parser Application")

def parse_hh_vacancies():
    url = "https://api.hh.ru/vacancies"
    params = {"text": "Python", "area": "1", "per_page": 10}  # Пример параметров запроса
    response = requests.get(url, params=params)
    data = response.json()

    for item in data['items']:
        job_format, _ = JobFormat.objects.get_or_create(name=item.get('schedule', {}).get('name', ''))
        vacancy, created = Vacancy.objects.get_or_create(
            title=item['name'],
            defaults={
                'description': item.get('snippet', {}).get('responsibility', ''),
                'company': item['employer']['name'],
                'salary': item.get('salary', {}).get('from', '') or item.get('salary', {}).get('to', ''),
                'link': item['alternate_url'],
                'posted_date': item['published_at'],
                'job_format': job_format,
                'schedule': item.get('schedule', {}).get('name', '')
            }
        )
        if created:
            for skill in item.get('key_skills', []):
                skill_obj, _ = Skill.objects.get_or_create(name=skill['name'])
                vacancy.skills.add(skill_obj)

def parse_form_view(request):
    if request.method == 'POST':
        form = ParseForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            area = form.cleaned_data['area']
            parse_hh_vacancies(request, keyword, area)
    else:
        form = ParseForm()

    return render(request, 'application/parse_form.html', {'form': form})

from django.db.models import Count

def vacancy_statistics_view(request):
    vacancies_count = Vacancy.objects.count()
    return render(request, 'statistics.html', {'vacancies_count': vacancies_count})

def search_vacancies_view(request):
    query = request.GET.get('q', '')
    vacancies = Vacancy.objects.filter(title__icontains=query)
    return render(request, 'search.html', {'vacancies': vacancies})

def vacancy_list_view(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'application/vacancy_list.html', {'vacancies': vacancies})

def run_parser(request):
    parse_hh_vacancies()
    return HttpResponse("Parser has been run.")