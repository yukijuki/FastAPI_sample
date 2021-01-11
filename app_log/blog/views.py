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

def home(request):
    context = {
        "posts" : posts,
        "title" : "passed"
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html")

