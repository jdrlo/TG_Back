from django.shortcuts import render
from django.http import Http404

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Reservas
from .serializer import ReservasSerializer
from rest_framework import viewsets, permissions

class ReservasViewSet(viewsets.ModelViewSet):
    queryset = Reservas.objects.all().order_by('-created')
    serializer_class = ReservasSerializer 
    permission_classes = [permissions.AllowAny]


    

