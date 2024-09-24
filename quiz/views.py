from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
import json
from .models import Quiz, Submission, SubmittedAnswer
from .forms import QuizForm, SubmissionForm, GradingForm
from question.models import Question, Answer
from module_group.models import Module, ModuleGroup  # Import the existing ModuleGroup model
from django.contrib import messages
from django.db.models import Q

@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    module_groups = ModuleGroup.objects.all()

    # Get the user's submissions for each quiz
    for quiz in quizzes:
        quiz.user_submission = Submission.objects.filter(quiz=quiz, student=request.user).first()

    return render(request, 'quiz_list.html', {'quizzes': quizzes, 'module_groups': module_groups})

@login_required
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.created_by = request.user
            quiz.save()
            selected_questions = request.POST.getlist('selected_questions')
            quiz.questions.set(selected_questions)
            return redirect('quiz:quiz_detail', quiz_id=quiz.id)
    else:
        form = QuizForm()

    return render(request, 'create_quiz.html', {'form': form})

@login_required
def edit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            quiz = form.save()
            selected_questions = request.POST.getlist('selected_questions')
            quiz.questions.set(selected_questions)
            messages.success(request, 'Quiz updated successfully.')
            return redirect('quiz:quiz_detail', quiz_id=quiz.id)
    else:
        form = QuizForm(instance=quiz)
    return render(request, 'edit_quiz.html', {'form': form, 'quiz': quiz})

@login_required
def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        quiz.delete()
        messages.success(request, 'Quiz deleted successfully.')
        return redirect('quiz:quiz_list')
    return render(request, 'delete_quiz.html', {'quiz': quiz})

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quiz_detail.html', {'quiz': quiz})

@login_required
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.quiz = quiz
            submission.student = request.user
            submission.save()

            for question in questions:
                answer_text = request.POST.get(f'answer_{question.id}')
                if answer_text:
                    SubmittedAnswer.objects.create(
                        submission=submission,
                        question=question,
                        text=answer_text
                    )

            submission.calculate_grade()
            return redirect('quiz:submission_result', submission_id=submission.id)
    else:
        form = SubmissionForm()

    return render(request, 'submit_quiz.html', {'quiz': quiz, 'form': form, 'questions': questions})

@login_required
def submission_result(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    submitted_answers = submission.submitted_answers.all().select_related('question')

    result_data = []
    for submitted_answer in submitted_answers:
        question = submitted_answer.question
        correct_answer = question.answers.filter(is_correct=True).first()
        result_data.append({
            'question': question.question_text,
            'user_answer': submitted_answer.text,
            'correct_answer': correct_answer.text if correct_answer else 'N/A',
            'is_correct': submitted_answer.text == correct_answer.text if correct_answer else False
        })

    context = {
        'submission': submission,
        'result_data': result_data,
        'grade': submission.grade
    }
    return render(request, 'submission_result.html', context)

@login_required
def make_question(request):
    subject = request.GET.get('subject')
    category = request.GET.get('category')

    questions = Question.objects.filter(
        Q(subject__id=subject) & Q(category__id=category)
    )

    return render(request, 'make_question.html', {'questions': questions})

@login_required
def load_questions(request):
    subject_id = request.GET.get('subject')
    category_id = request.GET.get('category')

    questions = Question.objects.filter(
        subject_id=subject_id,
        category_id=category_id
    )

    questions_data = []
    for question in questions:
        question_data = {
            'id': question.id,
            'text': str(question),  # Using __str__ method of the Question model
            'answers': [
                {
                    'id': answer.id,
                    'text': str(answer),  # Using __str__ method of the Answer model
                    'is_correct': answer.is_correct if hasattr(answer, 'is_correct') else False
                } for answer in question.answers.all()
            ]
        }
        questions_data.append(question_data)

    return JsonResponse({'questions': questions_data})

