from django.shortcuts import render

from rest_framework import viewsets

from .models import category_model
from .serializers import category_serielizer

# Create your views here.

class category_viewset(viewsets.ModelViewSet):
    queryset = category_model.objects.all()
    serializer_class = category_serielizer
