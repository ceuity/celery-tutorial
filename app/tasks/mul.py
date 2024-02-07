from app.setup import app


@app.task(name="tasks.mul")
def mul(x, y):
    return x * y
