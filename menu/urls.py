from django.urls import path
from .views import deux_plats_du_jour, deux_desserts_du_jour, menu_du_jour

urlpatterns = [
    path('deux-plats-du-jour/', deux_plats_du_jour, name='deux_plats_du_jour'),
    path('deux-desserts-du-jour/', deux_desserts_du_jour, name='deux_desserts_du_jour'),
    path('menu-du-jour/', menu_du_jour, name='menu_du_jour'),
]
