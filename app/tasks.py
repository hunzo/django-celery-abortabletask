from celery import shared_task
from celery.contrib.abortable import AbortableTask
from celery_progress.backend import ProgressRecorder

from core.celery import app

from time import sleep

@shared_task(bind=True, base=AbortableTask)
def Counter(self, count):
    progress_recorder = ProgressRecorder(self)
    for i in range(count):

        print(CeleryGetTask())

        print(self.is_aborted())

        if self.is_aborted():
            return f"task aborted: {self.request.id}"
        print(i)
        sleep(0.5)

        progress_recorder.set_progress(i + 1, count)
    
    return "done"

def CeleryGetTask():
    try:
        i = app.control.inspect().active()

    except Exception as e:
        i = {}

    celery_host = i.keys()
    # hostname =  for k in i

    hostname = ""
    for x in celery_host:
        hostname = x


    # get task id
    tasks = []
    for t in i[hostname]:
        tasks.append(t['id'])
    # print(tasks)

    return tasks