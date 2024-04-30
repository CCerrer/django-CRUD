import responses
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ItemTests(APITestCase):

    @responses.activate
    def test_get_all_items(self):
        responses.add(responses.GET, 'https://dev.codeleap.co.uk/careers/', json={"items": []}, status=200)
        url = reverse('careerItems:items-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"items": []})

    @responses.activate
    def test_create_item(self):
        url = reverse('careerItems:items-list')
        data = {'username': 'fooUsername', 'title': 'fooTitle', 'content': 'fooContent'}
        responses.add(responses.POST, 'https://dev.codeleap.co.uk/careers/', json=data, status=status.HTTP_201_CREATED)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    @responses.activate
    def test_get_item(self):
        data = {'username': 'fooUsername', 'title': 'fooTitle', 'content': 'fooContent'}
        responses.add(responses.GET, 'https://dev.codeleap.co.uk/careers/1/', json=data, status=status.HTTP_200_OK)
        url = reverse('careerItems:items-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)

    @responses.activate
    def test_update_item(self):
        updated_data = {'title': 'testTitle', 'content': 'testContent'}
        responses.add(responses.PATCH, 'https://dev.codeleap.co.uk/careers/1/', json=updated_data, status=status.HTTP_200_OK)
        url = reverse('careerItems:items-detail', kwargs={'pk': 1})
        response = self.client.patch(url, updated_data, format='json')

        self.assertEqual(response.data, updated_data)

    @responses.activate
    def test_delete_item(self):
        responses.add(responses.DELETE, 'https://dev.codeleap.co.uk/careers/1/', status=status.HTTP_204_NO_CONTENT)
        url = reverse('careerItems:items-detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)