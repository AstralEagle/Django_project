
from django.urls import path
from .views import GetTimeView

urlpatterns = [
    path('get-delivery-time/', GetTimeView.as_view(), name='get-delivery-time'),
]