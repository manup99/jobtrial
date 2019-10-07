from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout
from .models import Jobs
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import  login_required

class index(View):
    def get(self,request):
        if request.user.is_authenticated:
            job=Jobs.objects.filter(user=request.user)
            print(job)
            return render(request, 'app/index.html',{'jobs':job})

        else:
            return render(request, 'app/index.html', {'jobs': "heoioih"})
class UserCreate(View):
    form_name=UserForm
    def get(self,request):
        form=self.form_name(None)
        return render(request,'app/register.html',{'form':form})
    def post(self,request):
        form=self.form_name(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            user=User.objects.create_user(
                username,
                email,
                password
            )
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('app:index')
        return render(request,'app/register.html',{'form':form})
class Login(View):
    def get(self,request):
        return render(request,'app/login.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('app:index')
        else:
            x=User.objects.filter(username=username)
            if x.count():
                return render(request,'app/login.html',{'error':'Password is incorrect'})
            else:
                return render(request,'app/login.html',{'error':'Username is incorrect'})
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('app:login')
class PostJob(View,LoginRequiredMixin):
    @method_decorator(login_required(login_url='app:login'))
    def get(self,request):
        return render(request,'app/post.html')
    def post(self,request):
        user=request.user
        job_heading=request.POST['job_heading']
        company= request.POST['company']
        location=request.POST['location']
        start_date=request.POST['start_date']
        salary = request.POST['salary']
        apply_by = request.POST['apply_by']
        job_type = request.POST['job_type']
        available = request.POST['available']
        about_company = request.POST['about_company']
        about_job = request.POST['about_job']
        skills = request.POST['skills']
        requirements = request.POST['requirements']
        why_us = request.POST['why_us']
        x=Jobs(user=request.user,job_heading=job_heading,company=company,
                    location=location,start_date=start_date,
                    salary=salary,apply_by=apply_by,
                    job_type=job_type,available=available,
                    about_company=about_company,about_job=about_job,
                    skills=skills,requirements=requirements,
                    why_us=why_us)
        x.save()
        return redirect('app:index')







