from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    related_habit_and_reward,
    validate_is_nice_habit,
    validate_related_habit,
    validate_time_to_complete,
)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            validate_time_to_complete,
            related_habit_and_reward,
            validate_is_nice_habit,
            validate_related_habit,
        ]
