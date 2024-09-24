from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ForumQuestion, ForumComment, Reply
from .forms import ForumQuestionForm, ForumCommentForm, ReplyForm
from subject.models import Subject
from django.core.paginator import Paginator
from module_group.models import ModuleGroup, Module


def question_list(request):
    selected_subject_id = request.GET.get('subject_id')

    # Get all subjects for the dropdown
    subjects = Subject.objects.all()

    # Filter questions based on selected subject, or show all questions
    if selected_subject_id:
        questions = ForumQuestion.objects.filter(subject_id=selected_subject_id)
    else:
        questions = ForumQuestion.objects.all()

    questions = questions.order_by('-created_at')

    # Pagination logic: paginate questions, 5 per page
    paginator = Paginator(questions, 10)  # Show 10 questions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    module_groups = ModuleGroup.objects.all()
    module = Module.objects.all()

    return render(request, 'forum_question_list.html', {
        'page_obj': page_obj,  # Pass the paginated questions
        'subjects': subjects,  # Pass the subjects for the dropdown
        'selected_subject_id': int(selected_subject_id) if selected_subject_id else None,
        'module_groups': module_groups,
        'module': module,
        # To highlight the selected subject
    })

@login_required
def question_detail(request, pk):
    question = get_object_or_404(ForumQuestion, pk=pk)

    if request.method == 'POST':
        comment_form = ForumCommentForm(request.POST)
        reply_form = ReplyForm(request.POST)

        if 'submit_comment' in request.POST and comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.question = question
            comment.save()
            return redirect('forum:question_detail', pk=pk)

        elif 'submit_reply' in request.POST and reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.user = request.user

            # Check if replying to a comment or another reply
            if request.POST.get('comment_id'):
                reply.comment = ForumComment.objects.get(pk=request.POST.get('comment_id'))
            elif request.POST.get('reply_id'):
                reply.parent_reply = Reply.objects.get(pk=request.POST.get('reply_id'))

            reply.save()
            return redirect('forum:question_detail', pk=pk)

    comment_form = ForumCommentForm()
    reply_form = ReplyForm()

    return render(request, 'forum_question_detail.html', {
        'question': question,
        'comments': question.comments.all(),
        'comment_form': comment_form,
        'reply_form': reply_form,
    })

@login_required
def create_question(request):
    if request.method == 'POST':
        form = ForumQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('forum:question_list')
    else:
        form = ForumQuestionForm()
    return render(request, 'forum_create_question.html', {'form': form})
