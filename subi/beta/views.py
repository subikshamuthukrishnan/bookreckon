from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView 
from . import model
class betacls(APIView):
    def post(self, request):
        val = request.data.get('value')
        x=model.predict(val)
        return Response(x)
