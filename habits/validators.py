from rest_framework.exceptions import ValidationError

from habits import models


class LeftEmptyValidator:
    """
    Допускает заполнение определенного количества полей среди переданных
    """

    def __init__(self, fields, fields_amount=None):
        self.fields_amount = fields_amount or 1
        self.fields = fields

    def __call__(self, value):
        non_empty = 0
        for field in self.fields:
            if value.get(field):
                non_empty += 1

        if non_empty != self.fields_amount:
            fields_string = ", ".join(self.fields)
            raise ValidationError(
                f"Среди полей {fields_string} должно быть заполнено {self.fields_amount}."
                f"Вы заполнили {non_empty}"
            )


class PleasantHabitEmptyValidator(LeftEmptyValidator):
    """
    Допускает заполнение определенного количества полей среди переданных при условии, что привычка приятная
    """

    def __call__(self, value):
        if value.get("is_pleasant"):
            super().__call__(value)


class NotPleasantHabitEmptyValidator(LeftEmptyValidator):
    """
    Допускает заполнение определенного количества полей среди переданных при условии, что привычка полезная
    """

    def __call__(self, value):
        if not value.get("is_pleasant"):
            super().__call__(value)


class MaxTimeValidator:
    """
    Валидатор, ограничивающий максимальную продолжительность
    """

    def __init__(self, max_time, message=None):
        self.max_time = max_time
        self.message = (
            message
            or f"Продолжительность не должна превышать {self.max_time.total_seconds()} секунд"
        )

    def __call__(self, value):
        if value > self.max_time:
            raise ValidationError(self.message)


class IsPleasantValidator:
    """
    Проверяет, что привычка приятная
    """

    message = "В качестве связанной привычки можно указать только приятную привычку"

    def __call__(self, value):
        if value is not None:
            habit = models.Habit.objects.get(id=value)
            if not habit.is_pleasant:
                raise ValidationError(self.message)


class PeriodicityBetweenValidator:
    """
    Проверка периодичности на вхождение в диапазон
    """

    def __init__(self, _min, _max):
        self._min = _min
        self._max = _max

    def __call__(self, value):
        if value is not None:
            if not self._min <= value <= self._max:
                raise ValidationError(
                    f"Периодичность не может быть меньше {self._min} и больше {self._max} дней"
                )
