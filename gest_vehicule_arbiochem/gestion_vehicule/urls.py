from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='gestion_vehicule/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('save_register/', views.save_register, name='save_register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('connect/', views.connect, name='connect'),
]

