from io import BytesIO

from app.setup import app


@app.task(name="tasks.file.read")
def read_file(file: BytesIO):
    print(file.getvalue())
    return file


@app.task(name="tasks.file.write")
def write_file(file_path: str):
    buffer = BytesIO()
    with open(file_path, "rb") as f:
        buffer.write(f.read())
    return buffer
