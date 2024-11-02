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