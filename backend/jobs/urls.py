from django.urls import path
from . import views
urlpatterns = [
    path('all-jobs/', views.AllJobsList.as_view()),
    path('top-salary-jobs/', views.TopSalaryJobs.as_view())
]