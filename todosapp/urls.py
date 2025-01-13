from django.urls import path
from . import views
app_name = "todosapp"
urlpatterns = [
    path('login/', views.login , name = "login-page"),
    
    
    
    ]