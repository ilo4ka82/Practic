# Generated by Django 5.0.6 on 2024-07-01 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_vacancy_created_date_vacancy_link_vacancy_salary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
