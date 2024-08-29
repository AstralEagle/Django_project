from django.urls import path
from .views import register_view, login_view, logout_view, ajout_adresse
from .views import RegisterAPIView, CustomAuthToken, UserProfileAPIView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('ajout-adresse/', ajout_adresse, name='ajout_adresse'),
    path('api/register/', RegisterAPIView.as_view(), name='api_register'),
    path('api/login/', CustomAuthToken.as_view(), name='api_login'),
    path('api/profile/', UserProfileAPIView.as_view(), name='api_profile'),
]
