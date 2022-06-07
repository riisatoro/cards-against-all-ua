from uuid import uuid4

from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse

from tests.api_client import make_request

from authentication.models import User


class TestUserJoinRoom(TestCase):
    def setUp(self):
        self.password = make_password('random-password')

        self.owner = User.objects.create(
            username='owner',
            email=str(uuid4()) + '@example.com',
            password=self.password,
        )
        self.player_1 = User.objects.create(
            username='player_1',
            email=str(uuid4()) + '@example.com',
            password=self.password,
        )

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
            url=reverse('join_game'),
            expected_status=expected_status,
            data=data,
            user=user,
            method='POST'
        )

    def __assert_player_in(self, room_data, user):
        user = filter(
            lambda user: user.get('user', {}).get('username', None) == user.username,
            room_data['users']
        )
        self.assertIsNotNone(user)

    def test_create_rooms(self):
        room_data = self.__create_room(user=self.owner, expected_status=201)
        room_id = room_data.get('id', None)
        self.assertIsNotNone(room_id)
        self.__assert_player_in(room_data, self.owner)

        room_data = self.__create_room(self.owner, expected_status=422)
        self.assertIsNone(room_data.get('id', None))
        self.assertIsNotNone(room_data.get('detail', None))

    def test_join_rooms(self):
        room_data = self.__create_room(self.owner, expected_status=201)
        room_id = room_data.get('id', None)
        self.assertIsNotNone(room_id)
        self.__assert_player_in(room_data, self.owner)
    
        room_data = self.__join_room(self.player_1, expected_status=200)
        self.assertIsNotNone(room_data.get('id', None))
        self.__assert_player_in(room_data, self.player_1)

        self.__create_room(self.player_1, expected_status=422)
