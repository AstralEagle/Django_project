from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, UserLoginForm, AdresseForm
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, UserWithAdresseSerializer, AdresseSerializer
from django.contrib.auth import get_user_model

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

User = get_user_model()

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = response.data
        token, created = Token.objects.get_or_create(user=User.objects.get(id=user['id']))
        return Response({'user': user, 'token': token.key})

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data['token']
        user = User.objects.get(auth_token=token)
        return Response({'token': token, 'user': UserWithAdresseSerializer(user).data})

class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserWithAdresseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user