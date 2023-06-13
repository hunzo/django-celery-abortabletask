from django.shortcuts import render, redirect
from django.contrib import messages

from .tasks import Counter, CeleryGetTask

# Create your views here.


def Home(request):

    try:
        tasks = CeleryGetTask()
    except:
        tasks = []
    if request.method == "POST":
        code = request.POST.get("code")

        if not code.isnumeric():
            messages.error(request, f"Please enter number")
            return redirect("home")

        ret = Counter.delay(int(code))

        print(ret.task_id)

        messages.success(
            request, f"count: {code}, cancel: http://localhost:8000/celery-progress/{ret.task_id}")
        return redirect("home")

    context = {
        "tasks": tasks
    }
    return render(request, "home.html", context)


def Cancel(request, task_id):
    task = Counter.AsyncResult(task_id)
    task.abort()
    return redirect("home")
