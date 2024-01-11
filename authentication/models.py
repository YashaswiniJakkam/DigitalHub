from django.db import models
from django.contrib.auth.models import User
# from adminControl.models import ProblemStatements

class UserProfile(models.Model):
    # Define the possible roles
    ROLE_CHOICES = [
        ('none','None'),
        ('student', 'Student'),
        ('mentor', 'Mentor'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Mentor(models.Model):
    mentor_id = models.AutoField(primary_key=True) 
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    employee_id = models.CharField(max_length=20, verbose_name='Employee-ID')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=10, verbose_name='Phone Number')
    expertise = models.CharField(max_length=50, verbose_name='Expertise')
    college_name = models.CharField(max_length=100, verbose_name='College Name')
    department = models.CharField(max_length=50, choices=[
        ('CSE', 'Computer Science and Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('IT', 'Information Technology'),
        ('MECH', 'Mechanical Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('MET', 'Metallurgical Engineering'),
        ('CIVIL', 'Civil Engineering'),
    ], verbose_name='Department')
    years_of_experience = models.IntegerField(verbose_name='Years of Experience')

    def __str__(self):
        return self.full_name

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    student_id = models.CharField(max_length=20, verbose_name='Student-ID')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=10, verbose_name='Phone Number')
    university_name = models.CharField(max_length=100, verbose_name='University Name')
    college_name = models.CharField(max_length=100, verbose_name='College Name')
    department = models.CharField(max_length=50, choices=[
        ('CSE', 'Computer Science and Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('IT', 'Information Technology'),
        ('MECH', 'Mechanical Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('MET', 'Metallurgical Engineering'),
        ('CIVIL', 'Civil Engineering'),
    ], verbose_name='Department')
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    # selected_problem_statements = models.ManyToManyField(ProblemStatements, blank=True)

    def __str__(self):
        return self.full_name