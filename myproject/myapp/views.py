from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views import View
from django.db.models import F, Q, Count, Value as V, Avg, Max, Min
from django.db.models.functions import Length, Upper, Concat
from .models import *

from .forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, SetPasswordForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from .forms import CustomUserCreationForm  


class indexView(View):
    template_name = "index.html"

    def get(self, request):
        posts = Post.objects.all().order_by('-updated_at')
        categories = Category.objects.all()
        context = {'posts':posts, 'categories':categories}
        return render(request, self.template_name, context)
    
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

class CreatepostView(LoginRequiredMixin, View):
    template_name = "post.html"
    login_url = '/login/'
    def get(self, request):
        form = PostForm()
        form2 = CategoriesForm()
        return render(request, self.template_name, {'form': form, 'form2': form2})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # สร้างโพสต์แต่ยังไม่บันทึกลงฐานข้อมูล
            post.author = request.user       # ตั้งค่า author ให้เป็นผู้ใช้ที่ล็อกอินอยู่
            post.save()
            form.save()
            return redirect('index')  # เปลี่ยนไปยัง URL ที่ต้องการ
        return render(request, self.template_name, {'form': form})

class CategoriesAddView(LoginRequiredMixin, View):
    template_name = "post.html"
    login_url = '/login/'

    def post(self, request):
        form = CategoriesForm(request.POST)
        redirect_from = request.POST.get('redirect_from')  # ตรวจสอบจาก POST

        if form.is_valid():
            form.save()
            if redirect_from == 'edit':
                post_id = request.POST.get('post_id')  # รับ post_id จากฟอร์ม
                return redirect('edit_post', pk=post_id)  # เปลี่ยนไปที่ edit_post
            else:
                return redirect('createpost')  # ถ้าเป็นจาก create ให้กลับไปที่ create

        # หาก form ไม่ valid ให้แสดงฟอร์มใหม่
        form_post = PostForm()
        form2 = CategoriesForm()
        context = {
            "form": form_post,
            "form2": form2
        }
        return render(request, self.template_name, context)

class PostdetailView(LoginRequiredMixin, View):
    template_name = "postdetail.html"
    login_url = '/login/'
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        comment = Comment.objects.filter(post_id=post_id)
        comment_count = comment.count()
        context = {'post':post, 'comment': comment, 'comment_count': comment_count}
        return render(request, self.template_name, context)

class EditPostView(View):
    template_name = "edit_post.html"

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        form2 = CategoriesForm(instance=post)
        # ดึงเฉพาะ categories ที่โพสต์นี้เลือกไว้
        return render(request, self.template_name, {'form': form, 'post': post, 'form2':form2})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)

        return render(request, self.template_name, {'form': form, 'post': post})

class DeletePostView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('index')
    

class CreateCommentView(LoginRequiredMixin, View):
    login_url = '/login/'
    def post(self, request, post_id):
        user = request.user
        post = Post.objects.get(id=post_id)
        text = request.POST.get("text")
        delete = request.POST.get("delete")
        if text:
            Comment.objects.create(
                user = user,
                post = post,
                description = text,
                created_at = datetime.now()
            )
        elif delete:
            comment = Comment.objects.get(id = delete ,user = request.user)
            comment.delete()

        return redirect('postdetail', post_id = post_id)
