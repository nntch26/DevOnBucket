from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views import View
from django.db.models import F, Q, Count, Value as V, Avg, Max, Min
from django.db.models.functions import Length, Upper, Concat
from .models import *

from .forms import PostForm 

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from .forms import CustomUserCreationForm  


class indexView(View):

    template_name = "index.html"

    def get(self, request):
       
        return render(request, self.template_name)
    

# login & register

class LoginView(View):

    template_name = "login.html"

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {"form":form})
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        
        return render(request, self.template_name, {"form":form})
    

class RegisterView(View):
    
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {"form": form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        
        return render(request, 'register.html', {"form": form})
    


class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('index')



class CreatepostView(View):
    template_name = "post.html"

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # สร้างโพสต์แต่ยังไม่บันทึกลงฐานข้อมูล
            post.author = request.user       # ตั้งค่า author ให้เป็นผู้ใช้ที่ล็อกอินอยู่
            post.save()
            form.save()
            return redirect('index')  # เปลี่ยนไปยัง URL ที่ต้องการ
        return render(request, self.template_name, {'form': form})


class PostdetailView(View):
    
    template_name = "postdetail.html"
    def get(self, request):

        return render(request, self.template_name)
    
class CreateCommentView(View):
    def post(self, request, post_id):
        user = request.user
        post = Post.objects.get(id=post_id)
        text = request.POST.get("text")
        if text:
            Comment.objects.create(
                user = user,
                post = post,
                description = text,
                created_at = datetime.now()
            )

        return redirect('index')
    