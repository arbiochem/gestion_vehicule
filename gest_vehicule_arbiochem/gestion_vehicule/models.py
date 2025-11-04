from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    def save(self, *args, **kwargs):
        # Exemple : faire quelque chose avant de sauvegarder
        print("Sauvegarde de l'utilisateur :", self.username)
        
        # Appeler la méthode save() originale
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username or "Utilisateur sans nom"