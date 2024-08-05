from time import sleep

from app.setup import app


@app.task(name="tasks.wait")
def wait(x: int):
    sleep(x)

    return x
