from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model

User= get_user_model()

class Book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_year =models.PositiveIntegerField() 

    class Meta:
        permissions = [
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
            ("can_delete", "Can delete books"),
        ]
    def __str__(self):
        return self.title
    
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True,blank=True)
    profile_photo = models.ImageField(upload_to='profile_pics/',null=True,blank=True)
    
    def __str__(self):
        return self.username
    
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email= self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_pasworrd(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)