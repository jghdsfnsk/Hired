from django.shortcuts import render
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class AllApplicationsList(APIView):
    def get(self, request, format=None):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

class AllApplicationsbyJob(APIView):
    def get(self, request,username,job_slug, format=None):
        applications = Application.objects.filter(job__slug=job_slug).filter(user__username=username)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

class AllApplicationsbyUser(APIView):
    def get(self, request,username, format=None):
        applications = Application.objects.filter(user__username=username)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)