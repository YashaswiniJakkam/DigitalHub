from django.shortcuts import render, get_object_or_404, redirect
from adminControl.models import *
from authentication.models import *
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request, "./home/homepage.html")

def problemstatements(request):
	statements = ProblemStatements.objects.all()
	context = {'statements':statements,}
	return render(request, "./problemstatements/ProblemStatement.html", context=context)

def problem_statement_detail(request, slug):
	problem_statement = get_object_or_404(ProblemStatements, slug=slug)
	if request.user.is_authenticated:
		userrole = request.user.userprofile.role
	else: userrole = ""
	mentors = problem_statement.mentors_assigned.all()
	students = problem_statement.students_working_on.all()
	context = {'statement':problem_statement,'userrole':userrole,'mentors':mentors,'students':students}
	return render(request, 'problemstatements/probst.html', context)

def team(request):
	return render(request, "team/team.html")

def courses(request):
	return render(request, "./courses/courses.html")

@login_required
def dashboard(request):
	user = request.user
	
	if request.user.userprofile.role == "student":
		userdata = Student.objects.get(email=user.username)
		return render(request, "./dashboard/student_dash_board.html",{"data":userdata})
	elif request.user.userprofile.role == "mentor":
		userdata = Mentor.objects.get(email=user.username)
		return render(request, "./dashboard/mentor_profile.html",{"data":userdata})
	else:
		return render(request, "./dashboard/mentor_profile.html")

@login_required
def studentProblemStatementRegister(request):
	if request.method == 'POST':
		slug = request.POST.get('slug')
		problem_statement = get_object_or_404(ProblemStatements, slug=slug)
		if request.user.is_authenticated:
			student = Student.objects.get(email = request.user.username)
			if student.problems.all().count() < 2 and problem_statement.students_working_on.count() < 4:
				problem_statement.students_working_on.add(student)
			else:
				return HttpResponse("You have registered for 2 problemstatments")

				return redirect('/dashboard/myProblemStatements')
	return redirect(f'/problemstatements/')


@login_required
def mentorApply(request):
	if request.method == 'POST':
		slug = request.POST.get('slug')
		problem_statement = get_object_or_404(ProblemStatements, slug=slug)
		mentor = Mentor.objects.get(email = request.user.username)

		# if mentor.applied_problem_statements.count() < 2 and problem_statement.mentors_assigned.count() < 2:
		try:
			application = MentorApplication(mentor=mentor, problem_statement=problem_statement)
			application.save()
		except IntegrityError:
			return HttpResponse("You have already applied for this problem statement")  

	return redirect('/dashboard/myProblemStatements')

@login_required
def myProblemStatements(request):
	if request.user.userprofile.role == 'student':
		student = Student.objects.get(email = request.user.username)
		statements = student.problems.all()
	elif request.user.userprofile.role == 'mentor':
		mentor = Mentor.objects.get(email= request.user.username)
		statements = mentor.assigned_problem_statements.all()
	
	return render(request,'dashboard/myProblemStatements.html',{'statements':statements})
