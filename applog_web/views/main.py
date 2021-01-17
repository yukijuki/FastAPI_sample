from applog_web import app, templates
from fastapi import Request

@app.get("/")
async def index(request: Request):

    return templates.TemplateResponse("home.html", {"request": request})