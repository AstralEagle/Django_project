from django.urls import path
from .views import deux_plats_du_jour, deux_desserts_du_jour, menu_du_jour, confirmation_commande, passer_commande
from .views import MenuDuJourAPIView, PasserCommandeAPIView

urlpatterns = [
    path('deux-plats-du-jour/', deux_plats_du_jour, name='deux_plats_du_jour'),
    path('deux-desserts-du-jour/', deux_desserts_du_jour, name='deux_desserts_du_jour'),
    path('menu-du-jour/', menu_du_jour, name='menu_du_jour'),
    path('passer-commande/', passer_commande, name='passer_commande'),
    path('confirmation-commande/', confirmation_commande, name='confirmation_commande'),
    path('api/menu-du-jour/', MenuDuJourAPIView.as_view(), name='api_menu_du_jour'),
    path('api/passer-commande/', PasserCommandeAPIView.as_view(), name='api_passer_commande'),

]
