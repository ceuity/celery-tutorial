import os


class CeleryConfig(object):
    broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
    result_backend = os.environ.get("CELERY_BACKEND_URL", "redis://localhost:6379/0")
    task_serializer = "pickle"
    event_serializer = "pickle"
    result_serializer = "pickle"
    accept_content = ["application/json", "application/x-python-serialize"]
    enable_utc = False
    timezone = "Asia/Seoul"
