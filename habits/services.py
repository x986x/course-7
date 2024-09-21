import requests
from django.conf import settings


def send_telegram(message, chat_id):
    """
    Отправка одного сообщения в указанный чат телеграм
    """
    params = {
        "chat_id": chat_id,
        "text": message,
    }
    requests.post(url=settings.TELEGRAM_BOT_URL, json=params)


def send_habits_notifications(habits):
    """
    Отправка уведомлений в телеграм по переданным привычкам
    """
    for habit in habits:
        if habit.related_habit:
            reward = (
                f"Привычка {habit.related_habit.action}, "
                f"выполнить за {habit.related_habit.perform_in}"
            )
        else:
            reward = habit.reward

        message = (
            f"Время выполнять привычку!\n"
            f"Место: {habit.place}\n"
            f"Действие: {habit.action}\n"
            f"Награда: {reward}"
        )
        send_telegram(message, habit.user.telegram_chat_id)
