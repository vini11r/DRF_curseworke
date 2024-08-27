from rest_framework.serializers import ValidationError


def related_habit_and_reward(habit):
    if habit.get("related_habit") and habit.get("reward"):
        raise ValidationError(
            "Связанная привычка и вознаграждение не могут быть заданы одновременно."
        )


def validate_time_to_complete(habit):
    if habit.get("time_to_complete") and habit.get("time_to_complete") > 120:
        raise ValidationError("Время на выполнение не может превышать 120 сек.")


def validate_is_nice_habit(habit):
    if habit.get("is_nice_habit") and (
        habit.get("related_habit") or habit.get("reward")
    ):
        raise ValidationError(
            "Приятная привычка не может иметь связанную привычку или вознаграждение."
        )


def validate_related_habit(habit):
    if habit.get("related_habit"):
        if habit.get("is_nice_habit") is not True:
            raise ValidationError("Связанная привычка должна быть приятной.")
