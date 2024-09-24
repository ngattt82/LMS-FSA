from django.urls import path
from . import views

app_name = 'assignment'

urlpatterns = [
    path('list/', views.assignment_list, name='assignment_list'),
    path('create/', views.create_assignment, name='create_assignment'),
    path('edit/<int:assignment_id>/', views.edit_assignment, name='assignment_edit'),
    path('delete/<int:assignment_id>/', views.delete_assignment, name='assignment_delete'),
    path('detail/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),  # Add this line
    path('submit/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
    path('grade/<int:submission_id>/', views.grade_submission, name='grade_submission'),
    path('submissions/<int:assignment_id>/', views.submission_list, name='submission_list'),
    path('grades/', views.view_grades, name='view_grades'),
    path('submission/<int:submission_id>/', views.submission_detail, name='submission_detail'),
]
