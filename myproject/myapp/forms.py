from django.forms.widgets import Textarea, TextInput, SplitDateTimeWidget
from django.core.exceptions import ValidationError

from django import forms
from .models import *

from datetime import date, timedelta, time
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm


# ฟอร์ม Register
# class CustomUserCreationForm(UserCreationForm):

#     #  เพิ่มฟิลด์จากตารางอื่น เข้ามาในฟอร์มด้วย
#     phone_number = forms.CharField(max_length=10)
    
#     class Meta:
#         model = User
#         fields = [
#             'first_name',
#             'last_name', 
#             'username', 
#             'phone_number', 
#             'email', 
#             'password1', 
#             'password2'
#         ]
        

#     # เช็คว่าเบอร์ซ้ำมั้ย และต้องมี 10 หลัก ห้ามเป็นตัวอักษร
#     def clean_phone_number(self):
#         phone_number = self.cleaned_data["phone_number"]

#         data = UserDetail.objects.filter(phone_number= phone_number)

#         if data.count():  
#             raise ValidationError("Phone number Already Exist")

#         if len(phone_number) != 10 or not phone_number.isdigit():  
#             raise ValidationError("Phone number must have 10 digits")  

#         return phone_number  
    

#     # เช็คว่าอีเมลซ้ำมั้ย
#     def clean_email(self):
#         email = self.cleaned_data["email"]

#         data = User.objects.filter(email= email)

#         if data.count():  
#             raise ValidationError("Email Already Exist")  
#         return email  


