from rest_framework import serializers
from .models import Job
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', "email"]


class JobSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Job
        fields = [
            'owner', 
            'id', 
            'title', 
            'description', 
            'salary', 
            'city', 
            'state', 
            'created_on', 
            'slug'
            ]