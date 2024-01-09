from django.contrib import admin
from .models import *
# Register your models here.

class MentorDetails(admin.ModelAdmin):
	pass
class StudentDetails(admin.ModelAdmin):
	pass

admin.site.register(Mentor, MentorDetails)
admin.site.register(Student, StudentDetails)