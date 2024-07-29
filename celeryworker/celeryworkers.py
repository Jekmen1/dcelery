from celery import Celery

app = Celery("tasks")
app.conf.from_objects("celeryconfig")
app.conf.imports = ('newapp.tasks')
app.autodiscover_tasks()