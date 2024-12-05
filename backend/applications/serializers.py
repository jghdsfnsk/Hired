from rest_framework import serializers
from jobs.serializers import JobSerializer, UserSerializer
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    job = JobSerializer()
    class Meta:
        model = Application
        fields = [
            'user', 
            'job', 
            'description', 
            'created_at', 
            'rejected',
            'get_absolute_url'
            ]