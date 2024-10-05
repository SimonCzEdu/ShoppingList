from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    list_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts")
    
    def __str__(self):
        return f"{self.list_name}"