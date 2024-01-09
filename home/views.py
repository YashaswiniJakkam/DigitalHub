from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, "./home/homepage.html")

def problemstatements(request):
	return render(request, "./problemstatements/ProblemStatement.html")

def courses(request):
	return render(request, "./courses/courses.html")
def dashboard(request):
	return render(request, "./dashboard/student_dash_board.html")