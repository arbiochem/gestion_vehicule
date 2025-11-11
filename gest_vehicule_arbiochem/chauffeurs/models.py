from django.db import models

class Chauffeurs(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    voiture = models.CharField(max_length=100, blank=True, null=True)
    poste = models.CharField(max_length=100, blank=True, null=True)
    permis = models.CharField(max_length=50)
    lien = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'chauffeur'  # nom exact de la table

    def __str__(self):
        return f"{self.nom} {self.prenom}"

