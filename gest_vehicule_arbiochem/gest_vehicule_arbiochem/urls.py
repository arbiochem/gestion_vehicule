from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion_vehicule.urls')),
    path('chauffeur/', include('chauffeurs.urls', namespace='chauffeurs')),
]
