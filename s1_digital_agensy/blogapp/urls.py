from django.urls import path, include
from blogapp import views


app_name = 'blogapp'

urlpatterns = [
    path('', views.blog, name='blog'),
]
