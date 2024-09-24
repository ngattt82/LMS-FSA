from django.urls import path
from . import views
from training_program_subjects.views import view_subjects  # Add this import

app_name = 'training_program'
urlpatterns = [
    path('training_programs/', views.training_program_list, name='training_program_list'),
    path('training_programs/create/', views.training_program_add, name='training_program_add'),
    path('training_programs/edit/<int:pk>/', views.training_program_edit, name='training_program_edit'),
    path('training_programs/delete/<int:pk>/', views.training_program_delete, name='training_program_delete'),
    path('training_programs/<int:program_id>/manage_subjects/', views.manage_subjects, name='training_program_manage_subjects'),
    path('training_programs_subjects/<int:program_id>/view_subjects/', view_subjects, name='training_program_view_subjects'),
    path('enroll/<int:pk>/', views.training_program_enroll, name='training_program_enroll'),
    path('unenroll/<int:pk>/', views.training_program_unenroll, name='training_program_unenroll'),
    path('<int:pk>/users_enrolled/', views.users_enrolled, name='users_enrolled'),
]
