from django.contrib import admin
from django.urls import path, include
from application.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('application/', include('application.urls')),
]
