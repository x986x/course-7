from rest_framework import generics

from users import serializers


class RegistrationAPIVIew(generics.CreateAPIView):
    """
    Эндпоинт регистрации
    """

    serializer_class = serializers.RegistrationSerializer
