# application/parse.py

import requests
from .models import Vacancy, Skill, JobFormat

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
