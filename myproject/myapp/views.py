from django.shortcuts import render, redirect
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

# from .forms import CustomUserCreationForm  


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
            user1 = form.save()

            UserDetail.objects.create(
                user = user1, #ยัด obj user เข้าไป
                phone_number = form.cleaned_data['phone_number']
            )
            return redirect('login')
        
        return render(request, 'register.html', {"form": form})
    


class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('index')



class CreatepostView(View):
    
    template_name = "post.html"
    def get(self, request):

        return render(request, self.template_name)
    