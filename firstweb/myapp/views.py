from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Post


def home(request):
    # return HttpResponse("Hello : สวัสดี")
    all_post = Post.objects.all()

    context = {"all_post": all_post}

    return render(request, "myapp/home.html", context)
