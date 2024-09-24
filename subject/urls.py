from django.urls import path
from . import views

app_name = 'subject'
urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('add/', views.subject_add, name='subject_add'),
    path('edit/<int:pk>/', views.subject_edit, name='subject_edit'),
    path('subjects/delete/<int:pk>/', views.subject_delete, name='subject_delete'),
    path('subject/enroll/<int:pk>/', views.subject_enroll, name='subject_enroll'),
    path('unenroll/<int:pk>/', views.subject_unenroll, name='subject_unenroll'),
    path('resources/', views.resource_library, name='resource_library'),
    path('<int:pk>/detail/', views.subject_detail, name='subject_detail'),
    path('<int:pk>/enrolled/', views.users_enrolled, name='users_enrolled'),
    path('search/', views.course_search, name='course_search'),
    path('download/<str:file_type>/<int:file_id>/', views.file_download, name='file_download'),
]
