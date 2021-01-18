from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pyrebase

app = FastAPI()

app.mount("/static", StaticFiles(directory="./applog_web/static"), name="static")
templates = Jinja2Templates(directory="./applog_web/templates")

config = {
    "apiKey": "AIzaSyBP0h6ejdqQKuy8SNikN-Eea4Ol8cTApM0",
    "authDomain": "applog-ee503.firebaseapp.com",
    "databaseURL": "https://applog-ee503.firebaseio.com",
    "projectId": "applog-ee503",
    "storageBucket": "applog-ee503.appspot.com",
    "messagingSenderId": "1075416798765",
    "appId": "1:1075416798765:web:a4dabf43fa5aaa075b0aa4",
    "measurementId": "G-TJGVC5CZ0P"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()


from applog_web.views import get, post