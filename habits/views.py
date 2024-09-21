from rest_framework import generics, permissions as drf_permissions

from habits import models, serializers, permissions, paginators
from habits.models import Habit


class HabitListAPIView(generics.ListAPIView):
    """
    Базовый класс списка привычек
    """

    queryset = models.Habit.objects.all()
    serializer_class = serializers.HabitSerializer
    pagination_class = paginators.HabitPaginator


class UsersHabitListAPIView(HabitListAPIView):
    """
    Эндпоинт списка привычек текущего пользователя
    """

    permission_classes = [drf_permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListAPIView(HabitListAPIView):
    """
    Эндпоинт списка публичных привычек
    """

    queryset = Habit.objects.filter(is_public=True)


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Эндпоинт создания привычки
    """

    serializer_class = serializers.HabitSerializer
    permission_classes = [drf_permissions.IsAuthenticated]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Эндпоинт обновления привычки
    """

    serializer_class = serializers.HabitSerializer
    queryset = models.Habit.objects.all()
    permission_classes = [drf_permissions.IsAuthenticated, permissions.IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Эндпоинт удаления привычки
    """

    queryset = models.Habit.objects.all()
    permission_classes = [drf_permissions.IsAuthenticated, permissions.IsOwner]
