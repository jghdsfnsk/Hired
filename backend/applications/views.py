from django.shortcuts import render
from django.http import JsonResponse
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from rest_framework.decorators import authentication_classes, permission_classes
from django.core.mail import send_mail
from dotenv import load_dotenv
import os
# Create your views here.
load_dotenv(".env")
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

class ApplicationDetail(APIView):
    def get(self, request,username,job_slug,application_id, format=None):
        application = Application.objects.get(id=application_id)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)

def Send_Email(reciever, subject, message):
    sender_email = os.getenv('EMAIL')
    send_mail(subject, message, sender_email,[reciever], fail_silently=False)

@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def CreateApplication(request,username,job_slug):
    if request.method == 'POST':
        user = request.user
        job = Job.objects.get(slug=job_slug, owner__username=username)
        description = request.POST.get('desc')
        Send_Email(job.owner.email, f"New Application for {job.title}", f"New application from {user.username} for {job.title}")
        Send_Email(user.email, f"Application for {job.title}", f"Your application for {job.title} has been submitted")
        application = Application(user=user, job=job, description=description)
        application.save()
        return Response(status=status.HTTP_201_CREATED)