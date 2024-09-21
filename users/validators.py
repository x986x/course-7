from rest_framework.exceptions import ValidationError


class MatchingPasswordsValidator:
    """
    Валидатор для проверки совпадения двух введеных паролей
    """

    message = "Пароли не совпадают"

    def __call__(self, value):
        password1 = value.get("password")
        password2 = value.pop("password2", "")

        if password1 != password2:
            raise ValidationError(self.message)
