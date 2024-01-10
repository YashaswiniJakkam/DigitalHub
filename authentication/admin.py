from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profiles'

# Extend the UserAdmin to include UserProfile
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

class MentorDetails(admin.ModelAdmin):
	pass
class StudentDetails(admin.ModelAdmin):
	pass

# Register the extended User model
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)



admin.site.register(Mentor, MentorDetails)
admin.site.register(Student, StudentDetails)