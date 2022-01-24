from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAppiView(APIView):
    """Test API VIEW"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Users HTTP methods as fx (get, post, patch, put delete)',
            'Is similar to default dj view',
            'gives you the comst control of application logic',
            'is maaped manually to urls',
        ]

        return Response({'message':'Hello There',
        'an_apiview':an_apiview}) #when api is called it must retuen a response

