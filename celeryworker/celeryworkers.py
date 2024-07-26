from celery import Celery

app = Celery("tasks")
app.conf.from_objects("celeryconfig")

@app.task
def add_numbers():
    return
