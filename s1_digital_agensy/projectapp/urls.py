from django.urls import path, include
from projectapp import views


app_name = 'projectapp'


urlpatterns = [
    path('', views.project, name='projects'),
    # path('case/', views.case, name='case'),
    path('projects/case/<int:pk>/', views.case, name='case')
]
