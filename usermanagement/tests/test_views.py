from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from usermanagement.models import Role, UserProfile

User = get_user_model()


class UsersAPIViewTests(APITestCase):
    def setUp(self) -> None:
        Role.objects.create(role_name='student')
        # Semester.objects.create(semester_name='first')
        # Gender.objects.create(gender=0)
        # Faculty.objects.create(faculty_name='computer science')
        # City.objects.create(city_name='riyadh')

    def test_signup_api_view_is_working(self):
        url = reverse('usermanagement:signup_api_view')
        body = {
            "user": {
                "username": "ali",
                "password": "test45"
            },
            "email": "example@example.com",
            "first_name": "ali",
            "last_name": "khalil",
            "role": 1
        }
        response = self.client.post(url, body, format='json')
        self.assertEqual(response.status_code, 201)
        user = User.objects.filter(username=body['user']['username']).first()
        self.assertEqual(user.username, body['user']['username'])
        self.assertEqual(user.profile.email, body['email'])
        self.assertEqual(str(user.profile.gender), 'male')

    def test_signup_api_view_is_not_working_with_wrong_data(self):
        url = reverse('usermanagement:signup_api_view')
        body = {
            "username": "ali",
            "password": "test45",
            "email": "example@example.com",
            "first_name": "ali",
            "last_name": "khalil",
            "role": 5
        }
        response = self.client.post(url, body, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(UserProfile.objects.count(), 0)
