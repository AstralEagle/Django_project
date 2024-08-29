from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    path('accounts/', include('accounts.urls')),
    path('delivery/', include('delivery.urls')),  # Inclure les routes de l'application 'delivery'

]
