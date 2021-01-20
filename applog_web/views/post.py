from fastapi import Request, status, BackgroundTasks, Form
from fastapi.responses import JSONResponse, RedirectResponse
from applog_web import app, templates, db, auth, storage
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

@app.post("/project")
async def project(request: Request):
    if request.method == "POST":
        data = await request.form()
        project = data.get('project')
        print(project)
        return RedirectResponse("/screen",)
    
    return templates.TemplateResponse("project.html", {"request": request})
