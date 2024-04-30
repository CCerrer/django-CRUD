import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import ItemCreateSerializer, ItemUpdateSerializer, ItemSerializer

class ItemListView(APIView):
    @swagger_auto_schema(
            responses={
                200: openapi.Response('List retrieved successfully', ItemSerializer(many=True)),
                400: 'Bad Request'
            },
            operation_description='Get all items'
        )
    def get(self, request, *args, **kwargs):
        response = requests.get('https://dev.codeleap.co.uk/careers/')
        return Response(response.json(), status=response.status_code)
    
    @swagger_auto_schema(
            responses={
                201: openapi.Response('Item created successfully', ItemCreateSerializer),
                400: 'Bad Request'
            },
            request_body=ItemCreateSerializer,
            operation_description='Create a new item'
        )
    def post(self, request, *args, **kwargs):
        data = request.data
        response = requests.post('https://dev.codeleap.co.uk/careers/', json=data)
        return Response(response.json(), status=response.status_code)

class ItemDetailView(APIView):
    @swagger_auto_schema(
            responses={
                200: openapi.Response('Retrieval successful', ItemSerializer),
                404: 'Not Found'    
            },
            operation_description='Get a specific item by ID'
        )
    def get(self, request, pk, *args, **kwargs):
        response = requests.get(f'https://dev.codeleap.co.uk/careers/{pk}/')
        return Response(response.json(), status=response.status_code)

    @swagger_auto_schema(
            responses={
                200: openapi.Response('Update successful', ItemUpdateSerializer),
                404: 'Not Found'
            },
            request_body=ItemUpdateSerializer,
            operation_description='Update a specific item by ID'
        )
    def patch(self, request, pk, *args, **kwargs):
        data = {'title': request.data.get('title'), 'content': request.data.get('content')}
        response = requests.patch(f'https://dev.codeleap.co.uk/careers/{pk}/', json=data)
        return Response(response.json(), status=response.status_code)

    @swagger_auto_schema(
            responses={
                204: 'Deletion successful', 404: 'Not Found'},
            operation_description='Delete a specific item by ID'
        )
    def delete(self, request, pk, *args, **kwargs):
        response = requests.delete(f'https://dev.codeleap.co.uk/careers/{pk}/')
        return Response(response.json(), status=response.status_code)
