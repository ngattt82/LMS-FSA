from django.urls import path
from . import views

app_name = 'Course_Completion'

urlpatterns = [
    path('CourseCompletion/', views.CourseCompletion_list, name = 'CourseCompletion_list'),
]