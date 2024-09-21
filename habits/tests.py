from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from habits import models

User = get_user_model()


class HabitsTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.api_client = APIClient()
        cls.user = User(email="test@mail.com")
        cls.user.set_password("1234")
        cls.user.save()

        data = {
            "reward": "Тест 1",
            "periodicity": 7,
            "place": "at home",
            "perform_at": timezone.now().time(),
            "action": "Тест",
            "is_pleasant": False,
            "perform_in": timezone.timedelta(minutes=2),
            "is_public": False,
            "user": cls.user,
        }

        cls.habit = models.Habit.objects.create(**data)

    def test_create(self):
        data = {
            "reward": "Тест 2",
            "periodicity": 7,
            "place": "at home",
            "perform_at": "17:58:58.865860",
            "action": "Тест",
            "is_pleasant": False,
            "perform_in": "00:02:00",
            "is_public": False,
        }
        self.api_client.force_authenticate(self.user)
        response = self.api_client.post(reverse("habits:create"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(models.Habit.objects.filter(pk=2).exists())

    def test_list_user(self):
        self.api_client.force_authenticate(self.user)
        response = self.api_client.get(reverse("habits:list-user"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_public(self):
        self.api_client.force_authenticate(self.user)
        response = self.api_client.get(reverse("habits:list-public"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        self.api_client.force_authenticate(self.user)
        response = self.api_client.patch(
            reverse("habits:update", kwargs={"pk": 1}),
            data={
                "reward": "updated",
                "periodicity": 1,
                "perform_at": "17:58:58.865860",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.delete(
            reverse("habits:destroy", kwargs={"pk": 1}),
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
