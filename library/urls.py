
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add the 'home' view

    path('books/', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/add/', views.book_add, name='book_add'),

    path('authors/', views.author_list, name='author_list'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('author/add/', views.author_add, name='author_add'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Quiz paths
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:pk>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/add/', views.quiz_add, name='quiz_add'),
    path('quiz/<int:pk>/edit/', views.quiz_edit, name='quiz_edit'),
    path('quiz/<int:pk>/delete/', views.quiz_delete, name='quiz_delete'),

    # Question paths
    path('questions/', views.question_list, name='question_list'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/add/', views.question_add, name='question_add'),
    path('question/<int:pk>/edit/', views.question_edit, name='question_edit'),
    path('question/<int:question_pk>/answer/add/', views.answer_add, name='answer_add'),
    path('question/<int:pk>/delete/', views.question_delete, name='question_delete'),



]

