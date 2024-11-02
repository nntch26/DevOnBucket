from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, default="#FFFFFF")
    
    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return "{title} by {username}".format(title=self.title, username=self.author.username)
    
    def get_str_categories(self):
        cate_list = self.categories.values_list("name", flat=True)
        joined_string_comma = ', '.join(cate_list)
        return joined_string_comma
