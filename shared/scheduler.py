from celery.schedules import crontab

beat_scheduler = {
    "Slack_reminder_menu": {
        "task": "cornerapps.menu.tasks.send_reminder_menu",
        "schedule": crontab(minute='*'),
    },
}
