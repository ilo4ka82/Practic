from django.db import models
from django.utils import timezone

class JobFormat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    job_format = models.ForeignKey('JobFormat', on_delete=models.CASCADE)
    posted_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)
    schedule = models.CharField(max_length=50, null=True, blank=True)
    skills = models.ManyToManyField('Skill')

    def __str__(self):
        return self.title
