from django.urls import path
from . import views
import json


urlpatterns = [
    path('companies/',views.all_companies, name='companies'),
    path('companies/<int:company_id>/', views.company, name='company'),
    path('companies/id/vacancies', views.vacancy_by_company,name='vacancies'),
    path('vacancies/',views.all_vacancies),
    path('vacancies/id/',views.vacancy),
    path('vacancies/top_ten/', views.top_ten_vacancies, name='top_ten_vacancies'),
]