from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Team, UserProfile


class SimpleModelTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_team_and_user(self):
        t = Team.objects.create(name='marvel')
        u = UserProfile.objects.create(email='tony@stark.com', first_name='Tony', last_name='Stark', team=t)
        self.assertEqual(str(t), 'marvel')
        self.assertEqual(str(u), 'tony@stark.com')

    def test_api_root(self):
        url = reverse('api-root')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
