from django.contrib.auth import get_user_model
from rest_framework import serializers

from users import validators

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор регистрации
    """

    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email", "password", "password2", "telegram_chat_id"]
        validators = [validators.MatchingPasswordsValidator()]

    def save(self, *args, **kwargs):
        self.instance = User(
            email=self.validated_data.get("email"),
            telegram_chat_id=self.validated_data.get("telegram_chat_id"),
        )

        self.instance.set_password(self.validated_data.get("password"))
        self.instance.save()
        return self.instance
