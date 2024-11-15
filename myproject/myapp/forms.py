from django.forms.widgets import Textarea, TextInput, SplitDateTimeWidget
from django.core.exceptions import ValidationError

from django import forms
from .models import *

from datetime import date, timedelta, time
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(
        attrs={'placeholder': 'Write your post content here...',
                'class': 'content-area'}
    ))
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        
        labels = {
            'title': 'Post Title',
            'content': 'Content'
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'New post title here...', 
                                            'class': 'title-input'}),
        }


# ฟอร์ม Register
class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help texts
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''


    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2'
        ]
        

# เพิ่มประเภทข้อมูล
class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name"
        ]

