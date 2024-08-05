import os
from celery import Celery

from app import conf

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_BACKEND_URL = os.environ.get("CELERY_BACKEND_URL", "redis://localhost:6379/0")

app = Celery(__name__, broker=CELERY_BROKER_URL, backend=CELERY_BACKEND_URL)

app.conf.task_routes = {
    "tasks.mul": {"queue": "a_queue"},
    "tasks.sum": {"queue": "b_queue"},
    "tasks.wait": {"queue": "a_queue"},
    "tasks.human.*": {"queue": "a_queue"},
    "tasks.file.*": {"queue": "b_queue"},
}

### Config from object
app.config_from_object(conf.CeleryConfig)

### Set config directly
# app.conf.event_serializer = "pickle"
# app.conf.task_serializer = "pickle"
# app.conf.result_serializer = "pickle"
# app.conf.accept_content = ["application/json", "application/x-python-serialize"]
# app.conf.enable_utc = False
# app.conf.timezone = "Asia/Seoul"
