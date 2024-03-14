""" API Test cases """
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime
from .models import Swimmer, Date, Mark

class SwimmerAPITestCase(APITestCase):
    def setUp(self):
        self.swimmer_data = {
            'name': 'John Doe',
            'age': 25,
            'club': 'Example Club',
            'city': 'Example City'
        }
        self.swimmer = Swimmer.objects.create(**self.swimmer_data)
        self.list_url = reverse('swimmer-list')
        self.detail_url = reverse('swimmer-detail', kwargs={'pk': self.swimmer.pk})  

    def test_create_swimmer(self):
        response = self.client.post(self.list_url, self.swimmer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Swimmer.objects.count(), 2)  

    def test_retrieve_swimmer(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.swimmer_data['name'])
        self.assertEqual(response.data['age'], self.swimmer_data['age'])
        self.assertEqual(response.data['club'], self.swimmer_data['club'])
        self.assertEqual(response.data['city'], self.swimmer_data['city'])

    def test_update_swimmer(self):
        updated_data = {
            'name': 'Updated Name',
            'age': 30,
            'club': 'Updated Club',
            'city': 'Updated City'
        }
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.swimmer.refresh_from_db()
        self.assertEqual(self.swimmer.name, updated_data['name'])
        self.assertEqual(self.swimmer.age, updated_data['age'])
        self.assertEqual(self.swimmer.club, updated_data['club'])
        self.assertEqual(self.swimmer.city, updated_data['city'])

    def test_delete_swimmer(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Swimmer.objects.count(), 0)


class DateAPITestCase(APITestCase):
    def setUp(self):
        self.date_data = {
            'date': '2023-05-01',
            'active': True
        }
        self.date = Date.objects.create(**self.date_data)
        self.list_url = reverse('date-list')
        self.detail_url = reverse('date-detail', kwargs={'pk': self.date.pk})
    def test_create_date(self):
        response = self.client.post(self.list_url, self.date_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Date.objects.count(), 2)
    
    def test_retrieve_date(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['date'], self.date_data['date'])

    def test_update_date(self):
        updated_data = {
            'date': '2023-05-02',
            'active': False
        }
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.date.refresh_from_db()

        # Convert string date to datetime.date object
        updated_date = datetime.strptime(updated_data['date'], '%Y-%m-%d').date()        
        self.assertEqual(self.date.date, updated_date)
        #self.assertEqual(self.date.date, updated_data['date'])
        self.assertEqual(self.date.active, updated_data['active'])

    def test_delete_date(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Date.objects.count(), 0)

# class MarkAPITestCase(APITestCase):
#     def setUp(self):
#         self.mark_data = {
#             'mark': '10',
#             'date': '2023-05-01',
#             'swimmer': '1'
#         }
#         self.mark = Mark.objects.create(**self.mark_data)
#         self.list_url = reverse('mark-list')
#         self.detail_url = reverse('mark-detail', kwargs={'pk': self.mark.pk})

#     def test_create_mark(self):
#         response = self.client.post(self.list_url, self.mark_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Mark.objects.count(), 2)

#     def test_retrieve_mark(self):
#         response = self.client.get(self.detail_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['mark'], self.mark_data['mark'])

#     def test_update_mark(self):
#         updated_data = {
#             'mark': '9',
#             'date': '2023-05-02',
#             'swimmer': '2'
#         }
#         response = self.client.put(self.detail_url, updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.mark.refresh_from_db()
#         self.assertEqual(self.mark.mark, updated_data['mark'])
#         self.assertEqual(self.mark.date, updated_data['date'])
#         self.assertEqual(self.mark.swimmer, updated_data['swimmer'])

#     def test_delete_mark(self):
#         response = self.client.delete(self.detail_url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Mark.objects.count(), 0)
        
