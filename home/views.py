from django.shortcuts import render, get_object_or_404
from adminControl.models import *
from authentication.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	return render(request, "./home/homepage.html")

def problemstatements(request):
	statements = ProblemStatements.objects.all()
	context = {'statements':statements}
	return render(request, "./problemstatements/ProblemStatement.html", context=context)

def problem_statement_detail(request, slug):
	problem_statement = get_object_or_404(ProblemStatements, slug=slug)
	print(problem_statement.title)
	return render(request, 'problemstatements/probst.html', {'statement': problem_statement})

def courses(request):
	return render(request, "./courses/courses.html")

@login_required
def dashboard(request):
	user = request.user
	
	if request.user.userprofile.role == "student":
		userdata = Student.objects.get(email=user.username)
	elif request.user.userprofile.role == "mentor":
		userdata = Mentor.objects.get(email=user.username)
	return render(request, "./dashboard/student_dash_board.html",{"data":userdata})