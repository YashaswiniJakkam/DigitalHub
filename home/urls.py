from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("problemstatements/", views.problemstatements, name="problemstatements"),
    path("courses/", views.courses, name="courses"),
	path('problemstatements/<slug:slug>/', views.problem_statement_detail, name='problem_statement_detail'),
    path("dashboard", views.dashboard, name="dashboard"),
    
]
