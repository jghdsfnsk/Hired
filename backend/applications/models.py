from django.db import models
from jobs.models import Job
from django.contrib.auth.models import User
# Create your models here.

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rejected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} | Application for {self.job.title}"
    
    def get_absolute_url(self):
        return f'/{self.job.owner.username}/{self.job.slug}/applications/{self.id}/'