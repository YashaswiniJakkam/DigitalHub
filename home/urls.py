from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("problemstatements/", views.problemstatements, name="problemstatements"),
    path("courses/", views.courses, name="courses"),
    
]
