import os


class CeleryConfig(object):
    BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND_URL", "redis://localhost:6379/0")
    CELERY_TASK_SERIALIZER = "pickle"
    CELERY_EVENT_SERIALIZER = "pickle"
    CELERY_RESULT_SERIALIZER = "pickle"
    CELERY_ACCEPT_CONTENT = ["application/json", "application/x-python-serialize"]
    CELERY_TIMEZONE = "Asia/Seoul"
    CELERY_ENABLE_UTC = False
