from django.shortcuts import render
from .models import Job
from .serializers import JobSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class AllJobsList(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

class TopSalaryJobs(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all().order_by('-salary')[:3]
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)