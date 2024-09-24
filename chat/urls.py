from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('users/', views.user_list_view, name='user_list'),
    path('messages/<str:username>/', views.chat_view, name='chat_view'),
    path('send/', views.send_message_form, name='send_message_form'),  # New URL pattern
]
