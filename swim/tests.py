from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Club, Swimmer, Date, Mark, Category
from datetime import timedelta

class AuthenticatedAPITestCase(APITestCase):
    """ SuperUser for tests """
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='admin123'
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')



class ClubAPITestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()
        self.club = Club.objects.create(name="Club A", city="Buenos Aires")
        self.list_url = reverse('club-list')
        self.detail_url = reverse('club-detail', args=[self.club.id])

    def test_list_clubs(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Club A', str(response.data))

    def test_retrieve_club(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Club A")
        self.assertEqual(response.data['city'], "Buenos Aires")

    def test_create_club(self):
        data = {
            "name": "Club B",
            "city": "Córdoba"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Club.objects.count(), 2)
        self.assertEqual(Club.objects.get(id=response.data['id']).city, "Córdoba")

    def test_update_club(self):
        data = {
            "name": "Club A Updated",
            "city": "La Plata"
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.club.refresh_from_db()
        self.assertEqual(self.club.name, "Club A Updated")
        self.assertEqual(self.club.city, "La Plata")

    def test_delete_club(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Club.objects.count(), 0)

class SwimmerAPITestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()
        self.club = Club.objects.create(name="Club X", city="Rosario")
        self.swimmer = Swimmer.objects.create(
            name="Lucía Pérez",
            sex="F",
            age=15,
            club=self.club,
            city="Rosario"
        )
        self.list_url = reverse('swimmer-list')
        self.detail_url = reverse('swimmer-detail', args=[self.swimmer.id])

    def test_list_swimmers(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Lucía", str(response.data))

    def test_retrieve_swimmer(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Lucía Pérez")
        self.assertEqual(response.data['sex'], "F")
        self.assertEqual(response.data['age'], 15)
        self.assertEqual(response.data['club'], self.club.id)

    def test_create_swimmer(self):
        data = {
            "name": "Juan López",
            "sex": "M",
            "age": 17,
            "club": self.club.id,
            "city": "Santa Fe"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Swimmer.objects.count(), 2)
        self.assertEqual(Swimmer.objects.get(id=response.data['id']).name, "Juan López")

    def test_update_swimmer(self):
        data = {
            "name": "Lucía Actualizada",
            "sex": "F",
            "age": 16,
            "club": self.club.id,
            "city": "Paraná"
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.swimmer.refresh_from_db()
        self.assertEqual(self.swimmer.name, "Lucía Actualizada")
        self.assertEqual(self.swimmer.age, 16)
        self.assertEqual(self.swimmer.city, "Paraná")

    def test_delete_swimmer(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Swimmer.objects.count(), 0)

    def test_create_swimmer_missing_required_fields(self):
        data = {
            "sex": "M",
            "club": self.club.id,
            "city": "Santa Fe"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        self.assertIn('age', response.data)

    def test_invalid_sex_choice(self):
        data = {
            "name": "Invalido",
            "sex": "X",
            "age": 20,
            "club": self.club.id,
            "city": "Corrientes"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('sex', response.data)

class DateAPITestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()
        self.date_instance = Date.objects.create(
            date=timezone.now().date(),
            active=True
        )
        self.list_url = reverse('date-list')
        self.detail_url = reverse('date-detail', args=[self.date_instance.id])

    def test_list_dates(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("date" in item for item in response.data))

    def test_retrieve_date(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.date_instance.id)
        self.assertEqual(response.data['active'], True)

    def test_create_date(self):
        data = {
            "date": timezone.now().date(),
            "active": False
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Date.objects.count(), 2)
        self.assertEqual(response.data['active'], False)

    def test_update_date(self):
        new_date = timezone.now().date()
        data = {
            "date": new_date,
            "active": False
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.date_instance.refresh_from_db()
        self.assertEqual(self.date_instance.active, False)

    def test_partial_update_date(self):
        data = {
            "active": False
        }
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.date_instance.refresh_from_db()
        self.assertFalse(self.date_instance.active)

    def test_delete_date(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Date.objects.count(), 0)

    def test_create_date_missing_field(self):
        data = {
            "active": True
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('date', response.data)



class MarkAPITestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()
        self.club = Club.objects.create(name="Club Pinocho", city="Buenos Aires")
        self.swimmer = Swimmer.objects.create(
            name="Juan Pérez",
            sex="M",
            age=20,
            club=self.club,
            city="Buenos Aires"
        )
        self.date = Date.objects.create(date=timezone.now().date(), active=True)
        self.mark = Mark.objects.create(swimmer=self.swimmer, date=self.date, meters=50.5)
        self.list_url = reverse('mark-list')
        self.detail_url = reverse('mark-detail', args=[self.mark.id])

    def test_list_marks(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_mark(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.mark.id)
        self.assertEqual(float(response.data['meters']), 50.5)

    def test_create_mark(self):
        # ✅ Usa otra fecha para evitar duplicado
        new_date = Date.objects.create(date=self.date.date + timedelta(days=1), active=True)
        data = {
            "swimmer": self.swimmer.id,
            "date": new_date.id,
            "meters": 100.0
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mark.objects.count(), 2)
        self.assertEqual(float(response.data['meters']), 100.0)

    def test_create_mark_duplicate(self):
        # ❌ Mismo nadador y fecha: debe fallar
        data = {
            "swimmer": self.swimmer.id,
            "date": self.date.id,
            "meters": 60.0
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("non_field_errors", response.data)

    def test_update_mark(self):
        # ✅ Mismo nadador y fecha, pero cambiando solo meters (válido)
        data = {
            "swimmer": self.swimmer.id,
            "date": self.date.id,
            "meters": 200.0
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.mark.refresh_from_db()
        self.assertEqual(self.mark.meters, 200.0)

    def test_partial_update_mark(self):
        data = {
            "meters": 75.0
        }
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.mark.refresh_from_db()
        self.assertEqual(self.mark.meters, 75.0)

    def test_delete_mark(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Mark.objects.count(), 0)

    def test_create_mark_missing_fields(self):
        data = {
            "swimmer": self.swimmer.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('date', response.data)
        self.assertIn('meters', response.data)






class CategoryAPITestCase(AuthenticatedAPITestCase):
    def setUp(self):
        super().setUp()
        self.category = Category.objects.create(name="Juvenil", age_min=12, age_max=17)
        self.list_url = reverse('category-list')
        self.detail_url = reverse('category-detail', args=[self.category.id])

    def test_list_categories(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_category(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.category.id)
        self.assertEqual(response.data['name'], "Juvenil")

    def test_create_category(self):
        data = {
            "name": "Infantil",
            "age_min": 8,
            "age_max": 11
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(response.data['name'], "Infantil")

    def test_create_category_invalid_age_range(self):
        data = {
            "name": "Cadete",
            "age_min": 14,
            "age_max": 10
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)
        self.assertIn("'age_max' must be greater or equal than 'age_min'", str(response.data['non_field_errors']))

    def test_update_category(self):
        data = {
            "name": "Juvenil Actualizado",
            "age_min": 13,
            "age_max": 18
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, "Juvenil Actualizado")

    def test_partial_update_category(self):
        data = {"age_max": 20}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.age_max, 20)

    def test_delete_category(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)
