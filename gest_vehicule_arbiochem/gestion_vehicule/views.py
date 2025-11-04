
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import CustomUser
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    users = CustomUser.objects.all()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form,'users':users})

def home(request):
    return render(request, 'accounts/login.html')

def dashboard(request):
    user = request.user  # L'utilisateur connecté
    return render(request, 'dashboard.html', {'user': user})

def connect(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = CustomUser.objects.get(username=username)
        
        if not username or not password:
            error = "Veuillez remplir tous les champs"
        elif user.check_password(password):
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('dashboard')
        else:
            error = "L'utilisateur ou mot de passe incorrect !!!!"
            return redirect('home')

def save_register(request):
    error = None 
    username_val = '' 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        username_val = username 

        if not username or not password:
            error = "Veuillez remplir tous les champs"
        elif password != password1:
            error = "Les mots de passe ne correspondent pas, veuillez réessayer !"
        else:
            user = CustomUser(username=username)
            user.set_password(password)
            user.save()
            return redirect('register')
    return render(request, 'accounts/register.html', {'error': error, 'username_val': username_val})

            