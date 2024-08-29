from django.urls import path
from .views import register_view, login_view, logout_view, ajout_adresse

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('ajout-adresse/', ajout_adresse, name='ajout_adresse'),
]
