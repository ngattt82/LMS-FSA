from django.urls import path
from . import views

app_name = 'certificate'
urlpatterns = [
    path('certificate', views.certificate_list, name='certificate_list'),
    path('certificate/add/', views.certificate_add, name='certificate_add'),
    path('certificate/<int:pk>/', views.certificate_detail, name='certificate_detail'),
    path('certificate/<int:pk>/edit/', views.certificate_edit, name='certificate_edit'),
    path('certificate/<int:pk>/delete/', views.certificate_delete, name='certificate_delete'),
]