from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
