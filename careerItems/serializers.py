from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'username', 'created_datetime', 'title', 'content']
        read_only_fields = ['id', 'created_datetime']

class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['username', 'title', 'content']

class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'content']