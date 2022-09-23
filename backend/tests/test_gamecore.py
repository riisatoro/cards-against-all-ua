from cmath import exp
from uuid import uuid4

from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.urls import reverse

from gamecore.models import User
from gamecore.models import RoomModel
from tests.api_client import make_request


class TestCreateJoinLeaveRoom(TestCase):
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
        self.player_2 = User.objects.create(
            username='player_2',
            email=str(uuid4()) + '@example.com',
            password=self.password,
        )

    def __get_room(self, user, expected_status, data=None):
        return make_request(
            url=reverse('game'),
            user=user,
            expected_status=expected_status
        )

    def __create_room(self, user, expected_status, data=None):
        return make_request(
            url=reverse('game'),
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

    def __leave_room(self, user, expected_status):
        return make_request(
            method='POST',
            url=reverse('leave_game'),
            expected_status=expected_status,
            user=user,
        )

    def __is_player_in(self, room_data, user):
        expected_user = filter(
            lambda user_dict: user_dict.get('user', {}).get('username', None) == user.username,
            room_data['users']
        )

        users_found = len(list(expected_user))
        self.assertLessEqual(users_found, 1, 'Expect one user because of uniq username, a few found')
        return bool(users_found)

    def test_create_room(self):
        room_data = self.__create_room(user=self.owner, expected_status=200)
        room_id = room_data.get('id', None)
        self.assertIsNotNone(room_id)
        self.assertTrue(
            self.__is_player_in(room_data, self.owner)
        )

        room_data = self.__create_room(self.owner, expected_status=422)
        self.assertIsNone(room_data.get('id', None))
        self.assertIsNotNone(room_data.get('detail', None))

    def test_get_room(self):
        room_data = self.__create_room(user=self.owner, expected_status=200)
        fetched_data = self.__get_room(self.owner, expected_status=200)

        self.assertDictEqual(room_data, fetched_data)

        fetched_data = self.__get_room(self.player_1, expected_status=200)
        self.assertDictEqual(fetched_data, {})

    def test_join_room(self):
        room_data = self.__create_room(self.owner, expected_status=200)
        room_id = room_data.get('id', None)
        self.assertIsNotNone(room_id)
        self.assertTrue(
            self.__is_player_in(room_data, self.owner)
        )
    
        room_data = self.__join_room(self.player_1, expected_status=200)
        self.assertIsNotNone(room_data.get('id', None))
        self.assertTrue(
            self.__is_player_in(room_data, self.player_1)
        )

        room_data = self.__create_room(self.player_1, expected_status=422)
        self.assertIsNone(room_data.get('id', None))
        self.assertIsNotNone(room_data.get('detail', None))

        room_data = self.__join_room(self.player_1, expected_status=422)
        self.assertIsNone(room_data.get('id', None))
        self.assertIsNotNone(room_data.get('detail', None))

    def test_join_concrete_room(self):
        self.__create_room(self.player_2, expected_status=200)
        owner_room = self.__create_room(self.owner, expected_status=200)
        owner_room_id = owner_room.get('id', None)

        self.assertIsNotNone(owner_room_id)
        self.assertEqual(RoomModel.objects.count(), 2)

        player_1_room = self.__join_room(self.player_1, 200, data={'room_uuid': owner_room_id})
        owner_room = self.__get_room(self.owner, 200)

        self.assertDictEqual(player_1_room, owner_room)

    def test_leave_room(self):
        self.assertEqual(RoomModel.objects.count(), 0)
        self.__create_room(self.owner, expected_status=200)
        room_data = self.__join_room(self.player_1, expected_status=200)

        for user in [self.owner, self.player_1]:
            with self.subTest(msg=user):
                self.assertTrue(
                    self.__is_player_in(room_data, user)
                )
        self.assertFalse(
            self.__is_player_in(room_data, self.player_2)
        )
        self.assertEqual(RoomModel.objects.count(), 1)

        self.__leave_room(self.player_2, expected_status=422)
        self.__leave_room(self.player_1, expected_status=200)

        self.assertEqual(RoomModel.objects.count(), 1)
        self.__leave_room(self.player_1, expected_status=422)
        
        self.__leave_room(self.owner, expected_status=200)
        self.assertEqual(RoomModel.objects.count(), 0)
