from django.urls import path
from . import views
urlpatterns = [
    path('all-applications/', views.AllApplicationsList.as_view()),
    path('<str:username>/applications/', views.AllApplicationsbyUser.as_view()),
    path('<str:username>/<slug:job_slug>/applications/', views.AllApplicationsbyJob.as_view()),
    path('<str:username>/<slug:job_slug>/applications/<int:application_id>', views.ApplicationDetail.as_view())
]