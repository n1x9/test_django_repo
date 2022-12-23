from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
        # Patterns using views 
    path('login/', views.login, name="login"),
    path('register/', views.register, name='register'),

]