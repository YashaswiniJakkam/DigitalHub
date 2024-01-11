from django.contrib import admin
from .models import *
# Register your models here.

class ProblemStatementsControl(admin.ModelAdmin): 
	pass

class MentorApplicationAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'problem_statement', 'mentor_expertise' ,'is_approved')
    actions = ['approve_selected_applications', 'reject_selected_applications','unassign']

    def mentor_expertise(self, obj):
        return obj.mentor.expertise

    mentor_expertise.short_description = 'Mentor Expertise'  # Customize the column header
    def approve_selected_applications(self, request, queryset):
        for application in queryset:
            application.is_approved = True
            application.save()
            problem_statement = application.problem_statement
            problem_statement.mentors_assigned.add(application.mentor)
        self.message_user(request, f'Selected applications approved successfully.')

    def unassign(self, request, queryset):
        for application in queryset:
            application.is_approved = False
            application.save()
            problem_statement = application.problem_statement
            problem_statement.mentors_assigned.remove(application.mentor)
        self.message_user(request, f'Selected applications Unassigned successfully.')

    def reject_selected_applications(self, request, queryset):
        for application in queryset:
            application.delete()
        self.message_user(request, f'Selected applications rejected successfully.')

admin.site.register(MentorApplication, MentorApplicationAdmin)

admin.site.register(ProblemStatements,ProblemStatementsControl)