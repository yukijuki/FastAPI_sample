from django.shortcuts import render

posts = [
    {
        "author": "yuki",
        "title": "sample 1",
        "content":"none",
        "date_posted": "August"
    },
    {
        "author": "yuki",
        "title": "sample 2",
        "content":"none",
        "date_posted": "August"
    },
]

context = {
        "posts" : posts,
        "title" : "passed"
    }

def home(request):
    return render(request, "applog/home.html", context)

def upload(request):
    return render(request, "applog/upload.html", context)

