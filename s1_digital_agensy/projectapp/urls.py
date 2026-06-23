from django.urls import path, include
from projectapp import views


app_name = 'projectapp'


urlpatterns = [
    path('', views.project, name='projects'),
]
