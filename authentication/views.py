from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import *


def logout(request):
    auth.logout(request)
    return redirect("/")


def login(request):
    next_url = request.GET.get("next")
    if next_url:
        request.session["next_url"] = next_url
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]

        if username == "" and password == "":
            messages.error(request, "Username and password cannot be empty")
        else:
            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user=user)
                next_url = request.session.get("next_url")
                if next_url:
                    del request.session["next_url"]
                    return redirect(next_url)

                return redirect("/dashboard")
            else:
                messages.error(request, "Invalid username or password")
                return redirect(request.path_info)

    return render(request, "./authentication/login.html", {"messages": messages.get_messages(request)})

def mentorRegister(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        employee_id = request.POST.get('employee_id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')
        expertise = request.POST.get('domain')
        college_name = request.POST.get('college_name')
        department = request.POST.get('department')
        years_of_experience = request.POST.get('years_of_experience')
        print(full_name,email)

        if User.objects.filter(email=email).exists():
            return HttpResponse("Email is already registered. Please use a different email.")
        
        user = User.objects.create_user(username=email, email=email, password=password)

        user_profile = UserProfile.objects.create(
            user=user,
            role='mentor'
        )


        mentor = Mentor.objects.create(
            full_name=full_name,
            employee_id=employee_id,
            email=email,
            phone_number=phone_number,
            expertise=expertise,
            college_name=college_name,
            department=department,
            years_of_experience=years_of_experience
        )

        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth.login(request,user)

        return redirect('/dashboard')
    
    return render(request, './authentication/mentor.html')

def studentRegister(request):
    if request.method == 'POST':
        # Get form data
        full_name = request.POST['name']
        student_id = request.POST['rollno']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phoneno']
        university_name = request.POST['universityname']
        college_name = request.POST['collegename']
        department = request.POST['dept']
        date_of_birth = request.POST['dob']

        # Create a user in Django's authentication system
        user = User.objects.create_user(username=email, email=email, password=password)
        
        user_profile = UserProfile.objects.create(
            user=user,
            role='student'
        )

        # Create a Student instance
        student = Student.objects.create(
            full_name=full_name,
            student_id=student_id,
            email=email,
            phone_number=phone_number,
            university_name=university_name,
            college_name=college_name,
            department=department,
            date_of_birth=date_of_birth
        )

        # Log the user in
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('/dashboard')  
    return render(request, './authentication/student.html')

def ResetPassword(request , token):
    context = {}
    
    
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/auth/reset_password/{token}/')
            
            if new_password == "" or confirm_password == "":
                messages.success(request, "Please Enter the password ")
                return redirect(f'/auth/reset_password/{token}/')
            
                
            
            if  new_password != confirm_password:
                messages.success(request, 'Passwords do not match')
                return redirect(f'/auth/reset_password/{token}/')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/auth/login')
            
            
            
        
        
    except Exception as e:
        print(e)
    return render(request , 'reset_password.html' , context)



# def ForgetPassword(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
        
#         try:
#             user_obj = User.objects.get(username=username)
#             #print(user_obj)
#             #print(user_obj.email)
#         except User.DoesNotExist:
#             messages.error(request, 'No user found with this username.')
#             return redirect(request.path_info)
        
#         try:
#             profile_obj = Profile.objects.get(user=user_obj)
#         except ObjectDoesNotExist:
#             profile_obj = Profile.objects.create(user=user_obj, forget_password_token="")
        
#         token = str(uuid.uuid4())
#         profile_obj.forget_password_token = token
#         profile_obj.save()
        
#         send_forget_password_mail(user_obj.email,user_obj.first_name, token)
#         messages.success(request, 'Reset password email sent')
#         return redirect(request.path_info)
#     else:
#         return render(request, 'forget_password.html') 
    

#code for changing password
@login_required
def changepassword(request):
    return render(request,"authentication/changepassword.html")


@login_required
def changingpwd(request):
    if request.method == "POST":
        try:
            oldpassword = request.POST.get("oldPassword")
            newpass = request.POST.get("newPassword")
            newpass2 = request.POST.get("confirmPassword")
            # print(oldpassword,newpass,newpass2)
            
            user = request.user
            if user.check_password(oldpassword) :
                if(newpass == newpass2):
                    user.set_password(newpass)
                    user.save()
                        
                    messages.success(request, "Password Changed")
                    return redirect('/auth/login')
                else:
                    messages.error(request,'New passwords are not matching')
            else:
                messages.error(request,"your old password is Incorrect")
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
        except Exception as e:
            messages.error(request,e)
    # else:
    #     pass
    
    return render(request,"changepwd.html")