import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ItemListView(APIView):
    def get(self, request, *args, **kwargs):
        response = requests.get('https://dev.codeleap.co.uk/careers/')
        return Response(response.json(), status=response.status_code)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        response = requests.post('https://dev.codeleap.co.uk/careers/', json=data)
        if response.status_code == 201:
            return Response(response.json(), status=status.HTTP_201_CREATED)
        else:
            return Response(response.json(), status=response.status_code)

class ItemDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        response = requests.get(f'https://dev.codeleap.co.uk/careers/{pk}/')
        return Response(response.json(), status=response.status_code)

    def patch(self, request, pk, *args, **kwargs):
        data = {'title': request.data.get('title'), 'content': request.data.get('content')}
        response = requests.patch(f'https://dev.codeleap.co.uk/careers/{pk}/', json=data)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.json(), status=response.status_code)

    def delete(self, request, pk, *args, **kwargs):
        response = requests.delete(f'https://dev.codeleap.co.uk/careers/{pk}/')
        if response.status_code == 204:
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(response.json(), status=response.status_code)
