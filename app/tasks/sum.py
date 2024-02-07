from app.setup import app


@app.task(name="tasks.sum")
def sum(x, y):
    return x + y
