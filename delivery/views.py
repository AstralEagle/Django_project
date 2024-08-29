# delivery/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class GetTimeView(APIView):

    def get(self, request):
        address1 = request.GET.get('address1')
        address2 = request.GET.get('address2')
        
        if not address1 or not address2:
            return Response({'error': 'Deux adresses sont nécessaires.'}, status=status.HTTP_400_BAD_REQUEST)
        
        distance_km = self.calculate_distance(address1, address2)
        
        if distance_km is None:
            return Response({'error': 'Impossible de calculer la distance entre les adresses fournies.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        if distance_km <= 5:  
            return Response({'can_order': True, 'distance_km': distance_km})
        else:
            return Response({'can_order': False, 'distance_km': distance_km})
    
    def calculate_distance(self, address1, address2):
        try:
            geolocator = Nominatim(user_agent="delivery_service")
            
            location1 = geolocator.geocode(address1)
            location2 = geolocator.geocode(address2)
            
            if not location1 or not location2:
                return None

            coords_1 = (location1.latitude, location1.longitude)
            coords_2 = (location2.latitude, location2.longitude)
            
            distance_km = geodesic(coords_1, coords_2).kilometers
            
            return distance_km
        except Exception as e:
            print(f"Erreur lors du calcul de la distance: {e}")
            return None