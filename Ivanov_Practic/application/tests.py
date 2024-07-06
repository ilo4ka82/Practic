from django.test import TestCase
from django.urls import reverse
from .models import Vacancy, JobFormat

class VacancyModelTest(TestCase):
    def setUp(self):
        job_format = JobFormat.objects.create(name='Full-time')
        self.vacancy = Vacancy.objects.create(
            title='Test Vacancy',
            description='Test Description',
            company='Test Company',
            salary='1000 USD',
            link='http://example.com',
            job_format=job_format,
            posted_date='2023-01-01',
            created_date='2023-01-01',
            schedule='Full-time'
        )

    def test_vacancy_creation(self):
        self.assertEqual(self.vacancy.title, 'Test Vacancy')
        self.assertEqual(self.vacancy.company, 'Test Company')

class VacancyStatisticsViewTest(TestCase):
    def test_statistics_view(self):
        response = self.client.get(reverse('vacancy_statistics_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Vacancy Statistics')

class VacancySearchViewTest(TestCase):
    def test_search_view(self):
        response = self.client.get(reverse('search_vacancies_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Search Vacancies')
