from django.shortcuts import render

from rest_framework import viewsets

from .models import complaint_model
from .serializers import complaint_serielizer

# Create your views here.

class complaint_viewset(viewsets.ModelViewSet):
    queryset = complaint_model.objects.all()
    serializer_class = complaint_serielizer
