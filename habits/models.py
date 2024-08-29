from django.db import models

from config.settings import AUTH_USER_MODEL

IS_NICE_HABIT = (
    (True, "Да"),
    (False, "Нет"),
)
PERIODIC_HABIT = (
    ("daily", "Ежедневно"),
    ("in a day", "Через день"),
    ("in a two days", "Раз в три дня"),
    ("weekly", "Раз в неделю"),
)


class Habit(models.Model):
    owner = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Создатель привычки", blank=True,
        null=True
    )
    place = models.CharField(
        max_length=100,
        verbose_name="Место выполнения привычки",
        help_text="Где выполнять?",
    )
    time = models.TimeField(
        verbose_name="Время выполнения привычки", help_text="Во сколько выполнять?"
    )
    action = models.CharField(
        max_length=200, verbose_name="Действие", help_text="Что делать?"
    )
    is_nice_habit = models.BooleanField(
        default=False,
        verbose_name="Приятная привычка",
        help_text="Это приятна привычка?",
        choices=IS_NICE_HABIT,
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        default=None,
        blank=True,
        null=True,
    )
    periodicity = models.CharField(
        max_length=50,
        default=PERIODIC_HABIT[0][1],
        verbose_name="Периодичность",
        choices=PERIODIC_HABIT,
        help_text="Как часто выполнять?",
    )
    reward = models.CharField(
        max_length=150,
        verbose_name="Вознаграждение",
        help_text="Какая награда?",
        blank=True,
        null=True,
    )
    time_to_complete = models.PositiveSmallIntegerField(
        verbose_name="Время на выполнение",
        help_text="Введите время на выполнение не более 120 сек.",
        default=120,
    )
    is_public = models.BooleanField(verbose_name="Публичность", default=False)

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
