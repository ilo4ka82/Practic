from django.urls import path
from .views import parse_hh_vacancies, parse_form_view, vacancy_statistics_view, search_vacancies_view, vacancy_list_view, run_parser

urlpatterns = [
    path('parse/', parse_form_view, name='parse_form_view'),
    path('parse_hh/', parse_hh_vacancies, name='parse_hh_vacancies'),
    path('statistics/', vacancy_statistics_view, name='vacancy_statistics_view'),
    path('search/', search_vacancies_view, name='search_vacancies_view'),
    path('vacancies/', vacancy_list_view, name='vacancy_list'),
    path('run-parser/', run_parser, name='run_parser'),
]

