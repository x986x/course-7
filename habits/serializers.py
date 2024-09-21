from datetime import timedelta

from rest_framework import serializers

from habits import models, validators


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор привычки
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    related_habit = serializers.IntegerField(
        required=False, validators=[validators.IsPleasantValidator()]
    )
    periodicity = serializers.IntegerField(
        required=False, validators=[validators.PeriodicityBetweenValidator(1, 7)]
    )
    perform_in = serializers.DurationField(
        validators=[validators.MaxTimeValidator(max_time=timedelta(seconds=120))]
    )
    next_perform_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.Habit
        fields = "__all__"
        validators = [
            validators.NotPleasantHabitEmptyValidator(
                fields_amount=1,
                fields=[
                    "related_habit",
                    "reward",
                ],
            ),
            validators.NotPleasantHabitEmptyValidator(
                fields_amount=2,
                fields=[
                    "perform_at",
                    "periodicity",
                ],
            ),
            validators.PleasantHabitEmptyValidator(
                fields_amount=0,
                fields=[
                    "related_habit",
                    "reward",
                    "perform_at",
                    "periodicity",
                ],
            ),
        ]
