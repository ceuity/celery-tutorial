from celery import Task

from app.setup import app
from app.classes.human import Human


@app.task(name="tasks.human.create")
def create_human(name: str, age: str):
    return Human(name, age)


@app.task(name="tasks.human.get")
def get_human(human: Human):
    print(human)
    return human


class CustomTask(Task):
    def __call__(self, *args, **kwargs):
        print(f"Task {self.request.id} is being executed")
        return self.run(*args, **kwargs)

    def on_success(self, retval, task_id, args, kwargs):
        print(f"Task {task_id} succeeded with result: {retval}")

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print(f"Task {task_id} failed with exception: {exc}")


@app.task(name="tasks.human.get.custom", base=CustomTask)
def get_human_custom(human: Human = None):
    if human is None:
        raise ValueError("Human is None")
    print(human)
    return human
