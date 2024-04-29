from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from careerItems.models import Item

class ItemTests(APITestCase):
    def test_create_item(self):
        url = reverse('careerItems:items-list')
        data = {'username': 'fooUsername', 'title': 'fooTitle', 'content': 'fooContent'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Item.objects.get().username, 'fooUsername')

    def test_get_item(self):
        item = Item.objects.create(username='fooUsername', title='fooTitle', content='fooContent')
        url = reverse('careerItems:items-detail', kwargs={'pk': item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], item.username)

    def test_update_item(self):
        item = Item.objects.create(username='fooUsername', title='fooTitle', content='fooContent')
        url = reverse('careerItems:items-detail', kwargs={'pk': item.pk})
        data = {'username': 'testUsername', 'title': 'testTitle', 'content': 'testContent'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Item.objects.get().username, 'testUsername')

    def test_delete_item(self):
        item = Item.objects.create(username='fooUsername', title='fooTitle', content='fooContent')
        url = reverse('careerItems:items-detail', kwargs={'pk': item.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)