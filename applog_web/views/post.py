from fastapi import Request, status, BackgroundTasks
from fastapi.responses import JSONResponse
from applog_web import app, templates
import time
from datetime import datetime

def _run_task(name: str, id=None):
    time.sleep(3)
    with open("tasks_out.txt", mode="a") as file:
        now = datetime.now()
        content = f"{name} [{id}]: {now}¥n"
        file.write(content)

@app.post("/task/run/{name}/{id}")
async def task_run(name: str, id: int, background_tasks: BackgroundTasks):
    """takes in a task and write it into a file"""
    background_tasks.add_task(_run_task, name, id)
    return {"message": f"Task {name} ID {id} is being run .."}
