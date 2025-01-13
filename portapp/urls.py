# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name= "home-page"),
    path('about/', views.about , name= "about-page"),
    path('contact/', views.contact , name= "contact-page"),
    path('services/', views.services , name= "service-page"),
    path('portfolio/', views.portfolio , name= "portfolio-page"),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details-page'),
]
