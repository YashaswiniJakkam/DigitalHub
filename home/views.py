from django.shortcuts import render
from adminControl.models import *
# Create your views here.
def home(request):
	return render(request, "./home/homepage.html")

def problemstatements(request):
	statements = ProblemStatements.objects.all()
	context = {'statements':statements}
	return render(request, "./problemstatements/ProblemStatement.html", context=context)

def courses(request):
	return render(request, "./courses/courses.html")
def dashboard(request):
	return render(request, "./dashboard/student_dash_board.html")