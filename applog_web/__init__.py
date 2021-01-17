from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="./applog_web/static"), name="static")
templates = Jinja2Templates(directory="./applog_web/templates")

from applog_web.views import main, tasks