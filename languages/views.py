from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Language,Paradign, Programer
from .serializer import LanguageSerializer,ParadignSerializer,ProgramerSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ParadignView(viewsets.ModelViewSet):
    queryset = Paradign.objects.all()
    serializer_class = ParadignSerializer

class ProgramerView(viewsets.ModelViewSet):
    queryset = Programer.objects.all()
    serializer_class = ProgramerSerializer