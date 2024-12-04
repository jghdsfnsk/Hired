from django.urls import path
from . import views
urlpatterns = [
    path('all-jobs/', views.AllJobsList.as_view())
]