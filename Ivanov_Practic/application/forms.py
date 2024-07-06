from django import forms

class ParseForm(forms.Form):
    keyword = forms.CharField(label='Keyword', max_length=100)
    area = forms.CharField(label='Area', max_length=100)

class VacancySearchForm(forms.Form):
    keyword = forms.CharField(label='Keyword', max_length=100, required=False)
    company = forms.CharField(label='Company', max_length=100, required=False)

# http://localhost:8000/application/statistics/
# http://localhost:8000/application/search/