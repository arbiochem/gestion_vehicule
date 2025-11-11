from django.urls import path
from . import views

app_name = 'chauffeurs'

urlpatterns = [
    path('', views.chauffeur, name='chauffeur'),
    path('Ajouter/', views.ajouter_chauffeur, name='ajouter_chauffeur'),
    path('modifier/<int:pk>/', views.modifier_chauffeur, name='modifier_chauffeur'),
    path('supprimer/<int:pk>/', views.supprimer_chauffeur, name='supprimer_chauffeur'),
]
