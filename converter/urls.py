from django.urls import path
from . import views

urlpatterns = [
    path("convert/jpeg-to-png/", views.jpeg_to_png, name="jpeg_to_png"),
    path("convert/png-to-jpeg/", views.png_to_jpeg, name="png_to_jpeg"),
    path("", views.main, name="main"),
]
