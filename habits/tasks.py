from datetime import timedelta

from django.utils import timezone

from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def telegram_sending():
    time_now = timezone.localtime()
    habits = Habit.objects.filter(
        time__gt=time_now, time__lt=time_now + timedelta(minutes=1)
    )

    for habit in habits:
        send_telegram_message(
            habit.owner.tg_chat_id, f"Напоминаю про привычку {habit.action}"
        )
