from django.urls import path, include

# from . import views
# from django.conf.urls import handler404
from mainapp import views


# handler404 = views.custom_404_view

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.products, name='projects'),
    path('contacts/', views.contacts, name='contacts'),
    path('about_us/', views.about_us, name='about_us'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('cases/', views.cases, name='cases'),
    # path('404/', views.custom_404_view, name='404'),

]
