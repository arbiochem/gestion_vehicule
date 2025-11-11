
from django.shortcuts import render, redirect, get_object_or_404
from .models import Chauffeurs
from .forms import ChauffeurForm

# Liste des chauffeurs
def chauffeur(request):
    chauffeurs = Chauffeurs.objects.all()
    form = ChauffeurForm() 
    return render(request, 'chauffeurs/liste.html', {'chauffeurs': chauffeurs, 'form': form, 'action': 'Ajouter'})

# Créer un chauffeur
def ajouter_chauffeur(request):
    if request.method == 'POST':
        form = ChauffeurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chauffeurs:chauffeur')
    else:
        form = ChauffeurForm()
    return render(request, 'chauffeurs/formulaire.html', {'form': form, 'action': 'Ajouter'})

# Modifier un chauffeur
def modifier_chauffeur(request, pk):
    chauffeur = get_object_or_404(Chauffeurs, pk=pk)
    if request.method == 'POST':
        form = ChauffeurForm(request.POST, instance=chauffeur)
        if form.is_valid():
            form.save()
            return redirect('chauffeurs:chauffeur')
    else:
        form = ChauffeurForm(instance=chauffeur)
    return render(request, 'chauffeurs/formulaire.html', {'form': form, 'action': 'Modifier'})

# Supprimer un chauffeur
def supprimer_chauffeur(request, pk):
    chauffeur = get_object_or_404(Chauffeurs, pk=pk)
    if request.method == 'POST':
        chauffeur.delete()
        return redirect('chauffeurs:chauffeur')
    return render(request, 'chauffeurs/supprimer.html', {'chauffeur': chauffeur})



