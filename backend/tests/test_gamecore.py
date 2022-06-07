from uuid import uuid4

from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse

from tests.api_client import make_request

from authentication.models import User


class TestUserJoinRoom(TestCase):
    def setUp(self):
        self.password = 'random-password'
        user_data = [
            {
                'username': str(uuid4()),
                'email': str(uuid4()) + '@example.com',
                'password': make_password(self.password),
            }
            for _ in range(10)
        ]

        self.users = [
            User.objects.create(**data)
            for data in user_data
        ]

    def __create_room(self, user, expected_status, data=None):
        return make_request(
            url=reverse('create_game'),
            expected_status=expected_status,
            data=data,
            user=user,
            method="POST",
        )

    def __join_room(self, user, expected_status, data=None):
        return make_request(
            url=reverse('join_random_game'),
            expected_status=expected_status,
            data=data,
            user=user,
            method='POST'
        )

    def test_create_rooms(self):
        room_data = self.__create_room(user=self.users[0], expected_status=201)
        room_id = room_data.get('id', None)
        self.assertIsNotNone(room_id)

        room_data = self.__create_room(self.users[0], expected_status=422)
        self.assertIsNotNone(room_data.get('detail', None))

    # def test_join_rooms(self):
    #     room_data = self.__create_room(self.users[0], expected_status=201)
    #     room_id = room_data.get('id', None)
    #     self.assertIsNotNone(room_id)

