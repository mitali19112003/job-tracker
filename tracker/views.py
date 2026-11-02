from django.shortcuts import render
from rest_framework import viewsets
from .models import Application, Company
from .serializers import ApplicationSerializer, CompanySerializer

# Create your views here.
class ApplicationViewSet(viewsets.ModelViewSet):    
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer    

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer