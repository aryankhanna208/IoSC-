from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email :
            raise ValueError("Email must be there")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        extra_fields.setdefault('profile_picture', 'default/static')
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.TextField(max_length=255, null=False)
    last_name = models.TextField(max_length=255, null= False)
    college = models.TextField(max_length=255, null=False)
    enrollment_no = models.BigIntegerField(
        validators=[
            MaxValueValidator(9999999999),  # Adjust the maximum value as needed
            MinValueValidator(1000000000),  # Adjust the minimum value as needed
        ],
        unique=True,  # Optional, if enrollment numbers should be unique
    )
    program = models.TextField(max_length=255)
    profile_pic = models.ImageField(blank=True,upload_to='profiles', default='default.jpeg')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','enrollment_no']

    def get_full_name(self):
        return self.first_name+ self.last_name
    
    def get_short_name(self):
        return self.first_name
    
    def _str_(self):
        return self.email

class Events(models.Model):
    name = models.TextField(max_length=255, null=False)
    description = models.TextField(max_length=255)
    announcement_date = models.DateField(auto_now_add=True)
    last_registration_date = models.DateTimeField()
    event_date = models.DateTimeField()
    image1 = models.ImageField(upload_to='event', blank=True, null=True)
    image2 = models.ImageField(upload_to='event', blank=True, null=True)
    image3 = models.ImageField(upload_to='event', blank=True, null=True)
    image4 = models.ImageField(upload_to='event', blank=True, null=True)
    image5 = models.ImageField(upload_to='event', blank=True, null=True)


    def __str__(self) :
        return self.name

class Projects(models.Model):
    name = models.TextField(max_length=255, null=False)
    description = models.TextField(max_length=255)
    project_lead = models.ForeignKey(User, on_delete=models.PROTECT)  # Use appropriate on_delete
    project_link = models.URLField(max_length=255)
    image = models.ImageField(upload_to='project', blank=True, null=True)


    def __str__(self):
        return self.name

class Blog(models.Model):
    writer = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)




    
