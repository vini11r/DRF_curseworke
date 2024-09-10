from django.db.models.expressions import result
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com")
        self.habit = Habit.objects.create(
            owner=self.user, place="Home", time="12:00:00", action="Зарядка"
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit_detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)

    def test_habit_create(self):
        url = reverse("habits:habit_create")
        data = {
            "owner": self.user.pk,
            "place": "Home",
            "time": "12:00",
            "action": "Зарядка",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        url = reverse("habits:habit_update", args=(self.habit.pk,))
        data = {
            "place": "Work",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.get(pk=self.habit.pk).place, "Work")

    def test_habit_delete(self):
        url = reverse("habits:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse(
            "habits:habit_list",
        )
        response = self.client.get(url)
        data = response.json()
        print(data)
        result_list = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": self.habit.place,
                    "time": self.habit.time,
                    "action": self.habit.action,
                    "is_nice_habit": self.habit.is_nice_habit,
                    "periodicity": self.habit.periodicity,
                    "reward": self.habit.reward,
                    "time_to_complete": self.habit.time_to_complete,
                    "is_public": self.habit.is_public,
                    "owner": self.user.pk,
                    "related_habit": self.habit.related_habit,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result_list)
