from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        models = User
        fields = ['email', 'first_name', 'last_name', 'college', 'enrollment_no', 'program', 'profile_pic']

class UserCreateSerializer(UserCreateSerializer ):
    class Meta :
        models = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')

class EventsSerializer(serializers.ModelSerializer):
    class Meta :
        model = Events
        fields = '__all__'
    
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta :
        model = Projects
        fields = '__all__'
    
class BlogSerializer(serializers.ModelSerializer):
    class Meta :
        model = Blog
        fields = '__all__'
    