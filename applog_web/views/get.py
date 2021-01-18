from applog_web import app, templates
from fastapi import Request

@app.get("/")
async def home(request: Request):
    screens = [
        {
            "screen_id": "1",
            "screen_name": "p2phome",
            "screen_image_name": "screen_image1"
        },
        {
            "screen_id": "2",
            "screen_name": "p2phome",
            "screen_image_name": "screen_image1"
        },
    ]

    return templates.TemplateResponse("home.html", {"request": request, "screens": screens})

@app.get("/screen/{screen_id}")
async def log(request: Request, screen_id: str):
    logs = [
        {
            "log_id":"1",
            "event_name": "custom_event",
            "event_category": "p2p",
            "firebase_screenname": "p2p",
            "event_action": "action_bar_click",
            "event_label": None,
            "event_label2": None
        },
        {
            "log_id":"2",
            "event_name": "custom_event",
            "event_category": "p2p",
            "firebase_screenname": "p2p",
            "event_action": "action_bar_click",
            "event_label": None,
            "event_label2": None
        },
    ]

    image = {
        "screen_image_name": "1",
        "correspondence": [
            {
                "id": 1,
                "x": 100,
                "y": 100,
            },
            {
                "id": 2,
                "x": 200,
                "y": 200,
            },
            {
                "id": 3,
                "x": 300,
                "y": 300,
            },
        ]
    }

    return templates.TemplateResponse("log.html", {"request": request, "logs": logs, "image": image})

@app.get("/")
def upload(w: Request):
    screens = [
        {
            "screen_name": "p2phome",
            "screen_id": 1,
            "screen_image": "screen_image1"
        },
        {
            "screen_name": "p2phome",
            "screen_id": 1,
            "screen_image": "screen_image1"
        },
    ]

    return templates.TemplateResponse("home.html", {"request": request, "screens": screens})