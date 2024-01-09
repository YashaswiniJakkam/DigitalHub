from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Mentor(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    employee_id = models.CharField(max_length=20, verbose_name='Employee-ID')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=10, verbose_name='Phone Number')
    expertise = models.CharField(max_length=50, verbose_name='Expertise') # Should be choice list based on the available problemstatements
    college_name = models.CharField(max_length=100, verbose_name='College Name')
    department = models.CharField(max_length=50, verbose_name='Department') # should be a choice list of all the departments.
    years_of_experience = models.IntegerField(verbose_name='Years of Experience')

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    student_id = models.CharField(max_length=20, verbose_name='Student-ID')
    email = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=10, verbose_name='Phone Number')
    university_name = models.CharField(max_length=100, verbose_name='University Name')
    college_name = models.CharField(max_length=100, verbose_name='College Name')
    department = models.CharField(max_length=50, verbose_name='Department')
    date_of_birth = models.DateField(verbose_name='Date of Birth')

    def __str__(self):
        return self.full_name