from django.urls import reverse
from rest_framework.test import APITestCase
import json


class DBTests(APITestCase):
    def test_db_correct(self):
        url = reverse('get', args=[3, 2, 'C'])
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content),
            [{"id": 3,
             "idStudent": 3,
             "idDiscipline": 2,
             "mark": 'C'
        }])