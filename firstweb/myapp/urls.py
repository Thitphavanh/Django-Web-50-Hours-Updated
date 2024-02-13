from django.urls import path
from myapp.views import home, blog

urlpatterns = [
    path("", home, name="home-page"),
    path("blogs/", blog, name="blog-page"),
]
