from django import forms
from .models import Chauffeurs

class ChauffeurForm(forms.ModelForm):
    class Meta:
        model = Chauffeurs
        fields = ['nom', 'prenom', 'voiture', 'poste', 'permis', 'lien']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'voiture': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Voiture'}),
            'poste': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Poste'}),
            'permis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Permis'}),
            'lien': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Lien'}),
        }
