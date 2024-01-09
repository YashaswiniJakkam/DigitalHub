from django.contrib import admin
from .models import *
# Register your models here.

class ProblemStatementsControl(admin.ModelAdmin): 
	pass

admin.site.register(ProblemStatements,ProblemStatementsControl)