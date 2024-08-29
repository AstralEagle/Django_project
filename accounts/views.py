from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, UserLoginForm, AdresseForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if not hasattr(user, 'adresse'):
                    return redirect('ajout_adresse')
                return redirect('menu_du_jour')
            else:
                form.add_error(None, "Email ou mot de passe incorrect")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def ajout_adresse(request):
    if request.method == 'POST':
        form = AdresseForm(request.POST)
        if form.is_valid():
            adresse = form.save(commit=False)
            adresse.user = request.user
            adresse.save()
            return redirect('menu_du_jour')
    else:
        form = AdresseForm()
    return render(request, 'accounts/ajout_adresse.html', {'form': form})

