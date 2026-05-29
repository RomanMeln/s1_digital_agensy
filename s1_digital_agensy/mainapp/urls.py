from django.urls import path, include
from mainapp import views


app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.products, name='projects'),
    path('contacts/', views.contacts, name='contacts'),
    path('about_us/', views.about_us, name='about_us'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('cases/', views.cases, name='cases'),
    path('contact-us/', views.contact_us, name='contact-us')
]
