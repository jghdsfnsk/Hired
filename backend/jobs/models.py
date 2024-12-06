from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    owner = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    fulldescription = models.TextField()
    summary = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.title} - {self.owner.username}"
    
    def get_absolute_url(self):
        return f'/{self.owner.username}/{self.slug}/'